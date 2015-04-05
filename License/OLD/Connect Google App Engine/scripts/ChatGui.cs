// ====================================================================================================================
// GUI for the chat and player list area
// Created by Leslie Young
// http://plyoung.com or http://plyoung.wordpress.com/
// ====================================================================================================================

using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class ChatGui: MonoBehaviour 
{
	private float message_refresh = -1000f;
	private float friends_refresh = -1000f;
	private float players_refresh = -1000f;

	private Rect rectPopupWindow = new Rect(0, 0, 240, 240);
	private Rect rectWindow = new Rect(0, 0, 1000, 300);
	private Rect plrLstRect = new Rect(700, 50, 295, 245);
	private Vector2 plrListScrollPos = Vector2.zero;
	private Vector2 chatScrollPos = Vector2.zero;

	private bool has_friends = true;
	private bool showingFriendList = false;
	private int selectedPlayer = 0;
	private int selectedFriend = 0;
	private string nameInput = "";

	public enum State : int { offline, normal, addfriend, contact, waiting, msg }
	public State state = State.offline;
	private string winMsg = "";

	private int activeChannel = 0;
	private string chatInput = "";
	private string getChannelNames = "";

	// ----------------------------------------------------------------------------------------------------------------
	#region start / init

	void Start() 
	{
		state = State.offline;
		rectWindow.x = Screen.width / 2 - rectWindow.width / 2;
		rectWindow.y = Screen.height - rectWindow.height;
		rectPopupWindow.x = Screen.width / 2 - rectPopupWindow.width / 2;
		rectPopupWindow.y = 100;// Screen.height / 2 - rectPopupWindow.height / 2;

		CreateChatChannelGUI(Chat.MAIN_CHANNEL, 0, true);
	}

	public void ConnectChat()
	{
		message_refresh = Time.time;
		friends_refresh = -1000f;
		players_refresh = -1000f;

		// put message on publich channel (0)
		Chat.Instance.AddMessage(0, "Visit www.plyoung.com or plyoung.wordpress.com for more info.\n");

		state = State.normal;
		RefreshFriendList(true); // force a refresh of friends list now to find out if there are any friends
		RefreshPlayersList();
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region update

	void LateUpdate()
	{
		if (state == State.normal)
		{
			if (message_refresh + Game.Instance.ChatMsgRefreshTimeout < Time.time)
			{
				message_refresh = Time.time;
				SDNet.Instance.NormalRequest(Game.ServerUrl + "msgs/", OnNetChatMessages, null);
			}

			if (friends_refresh + Game.FRIENDS_REFRESH_TIMEOUTS < Time.time)
			{
				RefreshFriendList(false);
			}

			if (players_refresh + Game.FRIENDS_REFRESH_TIMEOUTS < Time.time)
			{
				RefreshPlayersList();
			}

			if (getChannelNames.Length > 0)
			{
				SDNet.Instance.NormalRequest(Game.ServerUrl + "cpm/", OnNetPmNames, new Dictionary<string, string> { 
					{ "n", getChannelNames },			// channels to get names for
				});
				getChannelNames = "";
			}
		}
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region gui

	void OnGUI()
	{
		if (state == State.offline) return;

		GUI.Window(10, rectWindow, GUI_ChatArea, "");
		switch (state)
		{
			case State.addfriend:
			case State.contact: rectPopupWindow=GUI.Window(11, rectPopupWindow, GUI_EnterName, ""); break;
			case State.waiting: rectPopupWindow=GUI.Window(11, rectPopupWindow, GUI_Wait, ""); break;
			case State.msg: rectPopupWindow=GUI.Window(11, rectPopupWindow, GUI_Msg, ""); break;
		}		
	}

	private void GUI_EnterName(int id)
	{
		if (state == State.addfriend) GUI.Label(new Rect(10, 40, 200, 20), "ADD FRIEND ...");
		if (state == State.contact) GUI.Label(new Rect(10, 40, 200, 20), "CONTACT PLAYER ...");
		GUI.Label(new Rect(10, 85, 200, 20), "Enter name:");
		nameInput = GUI.TextField(new Rect(20, 105, 200, 20), nameInput, 30);

		if (GUI.Button(new Rect(15, 185, 100, 30), "Cancel")) state = State.normal;
		if (GUI.Button(new Rect(125, 185, 100, 30), "SUBMIT"))
		{
			if (state == State.addfriend)
			{
				friends_refresh = 1000000; // dont want refresh until done here
				winMsg = "Please wait. Looking for your new friend.";
				state = State.waiting;
				SDNet.Instance.NormalRequest(Game.ServerUrl + "addf/", OnNetFriendAdded, new Dictionary<string, string> { { "u", nameInput } });
			}
			else if (state == State.contact)
			{
				winMsg = "Please wait. Creating private channel.";
				state = State.waiting;
				SDNet.Instance.NormalRequest(Game.ServerUrl + "cpm/", OnNetStartPm, new Dictionary<string, string> { { "u", nameInput } });
			}
		}
	}

	private void GUI_Wait(int id)
	{
		GUI.Label(new Rect(10, 40, 220, 180), winMsg);
	}

	private void GUI_Msg(int id)
	{
		GUI.Label(new Rect(10, 40, 220, 180), winMsg);
		if (GUI.Button(new Rect(15, 185, 100, 30), "Close")) state = State.normal;
	}

	private void GUI_ChatArea(int id)
	{
		GUI_Channels();
		GUI_PlayerList();
	}

	private void GUI_Channels()
	{
		//GUI.Box(new Rect(3, 50, 690, 215), "");
		
		// message input field and submit button
		chatInput = GUI.TextField(new Rect(3, 272, 600, 25), chatInput, 256);
		if (GUI.Button(new Rect(606, 272, 90, 25), "submit")) GUIChatSubmit();

		// channel buttons and messages from active channel
		Rect r = new Rect(3, 20, 150, 29);
		foreach (Chat.ChannelInfo channel in Chat.Instance.channels.Values)
		{
			if (GUI.Button(r, channel.name)) activeChannel = channel.id;
			r.x += 155;

			if (activeChannel == channel.id)
			{
				chatScrollPos = GUI.BeginScrollView(new Rect(3, 50, 690, 215), chatScrollPos, new Rect(0, 0, 690, 2000), false, true);
				GUI.TextArea(new Rect(0, 0, 690, 2000), channel.messages);
				GUI.EndScrollView();
			}
		}
	}

	private void GUI_PlayerList()
	{
		if (showingFriendList)
		{
			GUI.Box(plrLstRect, "Friends");
			if (Chat.Instance.friendNames != null)
			{
				//Rect r = new Rect(0, 0, plrLstRect.width - 20, 25f * Chat.Instance.friendNames.Length);
				//Rect r2 = new Rect(plrLstRect.x + 10, plrLstRect.y + 30, plrLstRect.width, plrLstRect.height - 30);
				//plrListScrollPos = GUI.BeginScrollView(r2, plrListScrollPos, r);
				//selectedFriend = GUI.SelectionGrid(r, selectedFriend, Chat.Instance.friendNames, 1);
				Rect r = new Rect(0, 0, 270, 25f * Chat.Instance.friendNames.Length);
				Rect r2 = r;
				if (r.height < 210) r.height = 210;
				plrListScrollPos = GUI.BeginScrollView(new Rect(700, 80, 295, 210), plrListScrollPos, r, false, true);
				selectedFriend = GUI.SelectionGrid(r2, selectedFriend, Chat.Instance.friendNames, 1);
				GUI.EndScrollView();
			}
		}
		else
		{
			GUI.Box(plrLstRect, "Online Players");
			if (Chat.Instance.playerNames != null)
			{
				//Rect r = new Rect(0, 0, plrLstRect.width - 20, 25f * Chat.Instance.playerNames.Length);
				//Rect r2 = new Rect(plrLstRect.x + 10, plrLstRect.y + 30, plrLstRect.width, plrLstRect.height - 30);
				//plrListScrollPos = GUI.BeginScrollView(r2, plrListScrollPos, r, false, true);
				//selectedPlayer = GUI.SelectionGrid(r, selectedPlayer, Chat.Instance.playerNames, 1);
				Rect r = new Rect(0, 0, 270, 25f * Chat.Instance.playerNames.Length);
				Rect r2 = r;
				if (r.height < 210) r.height = 210;
				plrListScrollPos = GUI.BeginScrollView(new Rect(700, 80, 295, 210), plrListScrollPos, r, false, true);
				selectedPlayer = GUI.SelectionGrid(r2, selectedPlayer, Chat.Instance.playerNames, 1);
				GUI.EndScrollView();
			}
		}

		// player list related buttons
		if (GUI.Button(new Rect(plrLstRect.x, 3, 120, 45), (showingFriendList?"show players":"show friends"))) showingFriendList = !showingFriendList;
		if (GUI.Button(new Rect(plrLstRect.x + 193, 3, 50, 45), "add\nfriend")) state = State.addfriend;
		if (GUI.Button(new Rect(plrLstRect.x + 245, 3, 50, 45), "del\nfriend"))
		{
			if (Chat.Instance.friendNames != null)
			{
				friends_refresh = 1000000; // dont want refresh until done here
				winMsg = "Please wait. Removing player from your friends list.";
				state = State.waiting;
				SDNet.Instance.NormalRequest(Game.ServerUrl + "delf/", OnNetFriendDeleted, new Dictionary<string, string> { { "u", Chat.Instance.friends[selectedFriend].id.ToString() } });
			}
			else
			{
				winMsg = "No friend selected to delete.";
				state = State.msg;
			}
		}
		if (GUI.Button(new Rect(plrLstRect.x + 130, 3, 60, 45), "contact"))
		{
			state = State.contact;
			if (showingFriendList && Chat.Instance.friendNames != null) nameInput = Chat.Instance.friendNames[selectedFriend];
			if (!showingFriendList && Chat.Instance.playerNames != null)
			{
				if (Chat.Instance.playerNames[selectedPlayer].ToLower().Equals(Game.Instance.name.ToLower()))
				{
					state = State.msg;
					winMsg = "Can't create private channel with yourself.";
				}
				else nameInput = Chat.Instance.playerNames[selectedPlayer];
			}
		}
	}

	private void GUIChatSubmit()
	{
		if (string.IsNullOrEmpty(chatInput)) return;

		string msg = chatInput;
		msg = msg.Replace("|", "").Trim();
		chatInput = "";

		// send message to channel
		Chat.Instance.AddMessage(activeChannel, Game.Instance.name + ": " + msg);

		// send the message to the server, the reply will be a list of messages that
		// was send to same channel by other players since my last check

		Game.Instance.Update_ChatMsgRefreshTimeout(false); // dec wait time cause Im expecting a reply soon
		message_refresh = Time.time;
		SDNet.Instance.NormalRequest(Game.ServerUrl + "msgs/", OnNetChatMessages, new Dictionary<string, string> { 
				{ "m", msg},						// message to send
				{ "c", activeChannel.ToString()}	// id of channel to send on
			});
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region net

	private void OnNetFriendList(SDNet.ReturnCode code, string res)
	{
		if (code == SDNet.ReturnCode.OK && res.Length > 0)
		{
			Chat.Instance.friends.Clear();

			// decode message
			char[] splitter = { '|' };
			string[] players = res.Split(splitter);
			splitter[0] = ',';
			foreach (string p in players)
			{
				if (string.IsNullOrEmpty(p)) continue;
				string[] v = p.Split(splitter);
				if (v.Length < 3) continue;
				int id = SDUtil.ParseInt(v[0], 0);
				if (id <= 0) continue;
				int status = SDUtil.ParseInt(v[1], 3);
				Chat.Instance.friends.Add(new Chat.ChatPlayer(id, status, v[2]));
			}

			has_friends = false;
			if (Chat.Instance.friends.Count > 0)
			{
				// sort friends
				Chat.Instance.friends.Sort(delegate(Chat.ChatPlayer f1, Chat.ChatPlayer f2) { return f1.name.CompareTo(f2.name); });
				has_friends = true;
			}

			Chat.Instance.UpdateNamesCache();
		}
	}

	private void OnNetPlayerList(SDNet.ReturnCode code, string res)
	{
		if (code == SDNet.ReturnCode.OK && res.Length > 0)
		{
			Chat.Instance.players.Clear();

			// decode message
			char[] splitter = { '|' };
			string[] players = res.Split(splitter);
			splitter[0] = ',';
			foreach (string p in players)
			{
				if (string.IsNullOrEmpty(p)) continue;
				string[] v = p.Split(splitter);
				if (v.Length < 3) continue;
				int id = SDUtil.ParseInt(v[0], 0);
				if (id <= 0) continue;
				int status = SDUtil.ParseInt(v[1], 3);
				Chat.Instance.players.Add(new Chat.ChatPlayer(id, status, v[2]));
			}

			if (Chat.Instance.players.Count > 0)
			{
				// sort players
				Chat.Instance.players.Sort(delegate(Chat.ChatPlayer f1, Chat.ChatPlayer f2) { return f1.name.CompareTo(f2.name); });
			}

			Chat.Instance.UpdateNamesCache();
		}
	}

	private void OnNetFriendAdded(SDNet.ReturnCode code, string res)
	{
		friends_refresh = Time.time; // reset it now so refresh can be called again when needed
		state = State.normal;
		if (code == SDNet.ReturnCode.OK)
		{
			// should find the new friend's name in reply, add him with 'unknown' status for now
			if (res.Length > 0)
			{
				string[] v = res.Split(new char[] { ',' });
				if (v.Length > 1)
				{
					int id = SDUtil.ParseInt(v[0], 0);
					if (id > 0)
					{
						Chat.Instance.friends.Add(new Chat.ChatPlayer(id, 3, v[1]));
						Chat.Instance.UpdateNamesCache();
					}
				}
			}			
			return;
		}
		winMsg = "Could not find the player you wish to add. The name must be 5 or more character in length. The search is not case sensitive but you must provide the correct and the complete name of the player to find.";
		state = State.msg;
	}

	private void OnNetFriendDeleted(SDNet.ReturnCode code, string res)
	{
		friends_refresh = Time.time; // reset it now so refresh can be called again when needed
		state = State.normal;

		if (code == SDNet.ReturnCode.OK)
		{
			// not gonna make unnecessary refresh call so remove the active player from
			// list since it should be the one that was selected for removal

			Chat.Instance.friends.RemoveAt(selectedFriend);
			Chat.Instance.UpdateNamesCache();
			selectedFriend = 0;
		}
	}

	private void OnNetStartPm(SDNet.ReturnCode code, string res)
	{
		state = State.normal;
		if (code == SDNet.ReturnCode.OK)
		{
			int id = SDUtil.ParseInt(res, 0);
			if (id > 0)
			{
				CreateChatChannelGUI(nameInput, id, true);
				return;
			}
		}

		winMsg = "Could not find the player you wish to contact. The name must be 5 or more character in length. The search is not case sensitive but you must provide the correct and the complete name of the player to find.";
		state = State.msg;
	}

	private void OnNetPmNames(SDNet.ReturnCode code, string res)
	{
		if (code == SDNet.ReturnCode.OK)
		{
			char[] splitter = { '|' };
			string[] chans = res.Split(splitter);
			splitter[0] = ',';
			foreach (string c in chans)
			{
				if (string.IsNullOrEmpty(c)) continue;
				string[] vals = c.Split(splitter);
				if (vals.Length < 2) continue;
				int cid = SDUtil.ParseInt(vals[0], 0);
				if (cid > 0)
				{

					Chat.ChannelInfo cci = Chat.Instance.Channel(cid);
					if (cci != null) cci.name = vals[1];
				}
			}
		}
	}

	private void OnNetChatMessages(SDNet.ReturnCode code, string res)
	{
		Game.Instance.Update_ChatMsgRefreshTimeout(true); // increase by default (will decr below if needed)
		message_refresh = Time.time;
		if (code == SDNet.ReturnCode.OK)
		{
			int chan_id = 0;
			char[] splitter = { '|' };
			string[] msgs = res.Split(splitter);
			foreach (string m in msgs)
			{
				if (string.IsNullOrEmpty(m)) continue;

				Game.Instance.Update_ChatMsgRefreshTimeout(false); // got a msg, dec wait time

				// check if it is a channel id
				if (m[0] == '*')
				{
					string sn = m.Substring(1);
					int num = SDUtil.ParseInt(sn, 0);
					if (num > 0)
					{	// seems to be valid channel id
						// check if channel exist, if not, create it now
						Chat.ChannelInfo chan = Chat.Instance.Channel(num);
						if (chan == null)
						{							
							CreateChatChannelGUI("pm-" + num, num, false);
							getChannelNames += "," + num; // will haveta ask server what the channel name is							
						}
						chan_id = num;
						continue;
					}
				}
				Chat.Instance.AddMessage(chan_id, m);
			}
		}
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region priv

	private void RefreshFriendList(bool forced)
	{
		friends_refresh = Time.time;
		if (has_friends || forced) // no reason to check if know the player dont have friends.. or when forced to check
			SDNet.Instance.NormalRequest(Game.ServerUrl + "listf/", OnNetFriendList, null);
	}

	private void RefreshPlayersList()
	{
		players_refresh = Time.time;
		SDNet.Instance.NormalRequest(Game.ServerUrl + "listp/", OnNetPlayerList, null);
	}

	private void CreateChatChannelGUI(string name, int id, bool active)
	{
		if (Chat.Instance.channels.ContainsKey(id))
		{
			if (active) activeChannel = id;
			return;
		}

		Chat.Instance.AddChannel(id, name);
		if (active) activeChannel = id;
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
}
