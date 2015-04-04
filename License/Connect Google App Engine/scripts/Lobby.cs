// ====================================================================================================================
// Lobby - this handles the registration and login (could also be for matchmaking and strating matches)
// Created by Leslie Young
// http://plyoung.com or http://plyoung.wordpress.com/
// ====================================================================================================================

using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class Lobby : MonoBehaviour 
{

	public ChatGui chat;

	private enum State : int { none = 0, waiting, login_window, reg_window, recoverpw_window, inlobby, gamekey_window }
	private State state = State.none;

	private string simple_console_text = "";
	private string loginEmailEdit = "demo@web.net";
	private string loginPasswEdit = "demo123";
	private string regEmailEdit = "";
	private string regPasswEdit = "";
	private string regPubNameEdit = "";
	private string recoverPwEdit = "";
	private string gamekeyEdit = "";
	private string news_text = "";

	private string waitMsg = "";
	private Rect rectWindow = new Rect(0, 0, 240, 240);

	private Texture2D advert = null;
	private bool emailNotify = false;
	private Vector2 scrollPos = Vector2.zero;

	// ----------------------------------------------------------------------------------------------------------------
	#region start / init

	void Start()
	{
		rectWindow.x = Screen.width / 2 - rectWindow.width / 2;
		rectWindow.y = 100; // Screen.height / 2 - rectWindow.height / 2;

		chat = gameObject.GetComponent<ChatGui>();

		// contact the game server and wait for a reply send to OnNetVersionReply

		state = State.waiting;
		simple_console_text += "Checking version ...";
		waitMsg = "Checking game version";
		StartCoroutine(SDNet.Instance.VersionCheck(OnNetVersionReply));
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region gui

	void OnGUI()
	{
		scrollPos = GUI.BeginScrollView(new Rect(0, 0, 380, 250), scrollPos, new Rect(0, 0, 380, 2000), false, true);
		GUI.TextArea(new Rect(0, 0, 380, 2000), simple_console_text, 1024); // a simple console to show what is going on in network code
		GUI.EndScrollView();

		if (Application.isEditor)
		{
			if (GUI.Button(new Rect(870, 5, 100, 30), "Dump Log")) SDUtil.DumpHTMLLog();
		}

		switch (state)
		{
			case State.waiting:
			{
				GUI.Window(0, rectWindow, GUI_WaitWindow, "");
			} break;
			case State.login_window:
			{
				GUI.Window(0, rectWindow, GUI_LoginWindow, "LOGIN");
			} break;
			case State.reg_window:
			{
				GUI.Window(0, rectWindow, GUI_RegisterWindow, "REGISTER");
			} break;
			case State.recoverpw_window:
			{
				GUI.Window(0, rectWindow, GUI_RecoverPWWindow, "RECOVER PASSWORD");
			} break;
			case State.gamekey_window:
			{
				GUI.Window(0, rectWindow, GUI_GameKeyWindow, "UNLOCK GAME");
			} break;
		}

		if (state == State.inlobby && (chat.state==ChatGui.State.normal||chat.state==ChatGui.State.offline))
		{	
			// news
			GUI.BeginGroup(new Rect(0, 260, 380, 200));
			GUI.Box(new Rect(0, 0, 380, 200), "news sample");
			GUI.TextArea(new Rect(2, 30, 378, 168), news_text, 1024);
			GUI.EndGroup();

			// advert
			GUI.BeginGroup(new Rect(640,0,220,300));
				GUI.Box(new Rect(0,0,220,300), "advert sample");
				if (advert == null) GUI.Label(new Rect(50, 50, 100, 30), "loading ...");
				else GUI.Box(new Rect(0, 30, 220,270), advert);
			GUI.EndGroup();

			// settings
			GUI.BeginGroup(new Rect(400, 0, 220, 300));
			GUI.Box(new Rect(0, 0, 220, 150), "settings sample");
				emailNotify = GUI.Toggle(new Rect(5, 50, 210, 30), emailNotify, "Notify via e-mail");
				if (GUI.Button(new Rect(5, 100, 210, 30), "save settings"))
				{
					state = State.waiting;
					simple_console_text += "Saving settings online ...";
					waitMsg = "Saving settings online";
					Game.Instance.opt_email_notify = (emailNotify ? 1 : 0);
					SDNet.Instance.PriorityRequest(Game.ServerUrl + "settings/", OnNetSettingsSaved, new Dictionary<string, string> { 
						{ "email_notify", Game.Instance.opt_email_notify.ToString() },
					});
				}

			GUI.Box(new Rect(0, 150, 220, 150), "shop sample");			
				// a 1 in the string means the player owns the game
				GUI.Label(new Rect(5, 200, 220, 60), (Game.Instance.owns.Contains("1")?"The full game is unlocked":"This is a demo version"));
				if (GUI.Button(new Rect(5, 250, 210, 30), "Enter Game Key")) state = State.gamekey_window;
			GUI.EndGroup();
		}
	}

	private void GUI_WaitWindow(int id)
	{
		GUI.Label(new Rect(10, 40, 220, 180), waitMsg);
	}

	private void GUI_LoginWindow(int id)
	{
		GUI.Label(new Rect(10, 40, 200, 20), "Enter e-mail address:");
		loginEmailEdit = GUI.TextField(new Rect(20, 60, 200, 20), loginEmailEdit, 60);
		GUI.Label(new Rect(10, 85, 200, 20), "Enter password:");
		loginPasswEdit = GUI.PasswordField(new Rect(20, 105, 200, 20), loginPasswEdit, "*"[0], 30);

		if (GUI.Button(new Rect(70, 145, 100, 30), "LOGIN"))
		{
			state = State.waiting;
			simple_console_text += "Processing login ...";
			waitMsg = "Processing login";
			StartCoroutine(SDNet.Instance.Login(OnNetLogin, loginEmailEdit, loginPasswEdit));
		}

		if (GUI.Button(new Rect(15, 190, 100, 30), "Register")) state = State.reg_window;
		if (GUI.Button(new Rect(125, 190, 100, 30), "Recover PW")) state = State.recoverpw_window;
	}

	private void GUI_RegisterWindow(int id)
	{
		GUI.Label(new Rect(10, 40, 200, 20), "Enter e-mail address (for login):");
		regEmailEdit = GUI.TextField(new Rect(20, 60, 200, 20), regEmailEdit, 60);
		GUI.Label(new Rect(10, 85, 200, 20), "Enter password:");
		regPasswEdit = GUI.PasswordField(new Rect(20, 105, 200, 20), regPasswEdit, "*"[0], 30);
		GUI.Label(new Rect(10, 130, 200, 20), "Enter public name (visible name):");
		regPubNameEdit = GUI.TextField(new Rect(20, 150, 200, 20), regPubNameEdit, 30);

		if (GUI.Button(new Rect(15, 185, 100, 30), "Cancel")) state = State.login_window;
		if (GUI.Button(new Rect(125, 185, 100, 30), "REGISTER"))
		{
			// first do some checks to see if fields are valid before sending request over network

			if (string.IsNullOrEmpty(regEmailEdit)) { simple_console_text += "ERROR: Please enter a valid e-mail address. This is important to retrieve your password if you forget it.\n"; return; }
			if (regEmailEdit.Length < 3 || !Regex.IsMatch(regEmailEdit, @"^.+@[^.].*\.[a-z]{2,10}$", RegexOptions.IgnoreCase)) {
				simple_console_text += "ERROR: Please enter a valid e-mail address. This is important to retrieve your password if you forget it.\n"; 
				return; 
			}

			if (string.IsNullOrEmpty(regPasswEdit)) { simple_console_text += "ERROR: Please enter a password of between 5 and 15 characters.\n"; return; }
			if (regPasswEdit.Length < 5 || regPasswEdit.Length > 15) { simple_console_text += "ERROR: Please enter a password of between 5 and 15 characters.\n"; return; }

			if (string.IsNullOrEmpty(regPubNameEdit)) { simple_console_text += "ERROR: Please enter a public name of between 5 and 15 characters. Only letters and numbers allowed.\n"; return; }
			if (regPubNameEdit.Length < 5 || regPubNameEdit.Length > 15 || !Regex.IsMatch(regPubNameEdit, @"^[\w.-]+$", RegexOptions.IgnoreCase)) {
				simple_console_text += "ERROR: Please enter a public name of between 5 and 15 characters. Only letters and numbers allowed.\n"; 
				return; 
			}

			// call the registration function and wait for reply on OnNetRegisterReply
			state = State.waiting;
			simple_console_text += "Processing registration ...";
			waitMsg = "Processing registration";
			StartCoroutine(SDNet.Instance.Register(OnNetRegisterReply, regEmailEdit, regPasswEdit, regPubNameEdit));
		}
	}

	private void GUI_RecoverPWWindow(int id)
	{
		GUI.Label(new Rect(10, 40, 200, 20), "Enter e-mail address:");
		recoverPwEdit = GUI.TextField(new Rect(20, 60, 200, 20), recoverPwEdit, 60);
		if (GUI.Button(new Rect(15, 185, 100, 30), "Cancel")) state = State.login_window;
		if (GUI.Button(new Rect(125, 185, 100, 30), "SUBMIT"))
		{
			state = State.waiting;
			simple_console_text += "Processing request ...";
			waitMsg = "Processing request";
			StartCoroutine(SDNet.Instance.RecoverPW(OnNetRecoverPW, recoverPwEdit));
		}
	}

	private void GUI_GameKeyWindow(int id)
	{
		GUI.Label(new Rect(10, 40, 200, 20), "Enter gamekey:");
		gamekeyEdit = GUI.TextField(new Rect(20, 60, 200, 20), gamekeyEdit, 12);
		if (GUI.Button(new Rect(15, 185, 100, 30), "Cancel")) state = State.inlobby;
		if (GUI.Button(new Rect(125, 185, 100, 30), "SUBMIT"))
		{
			state = State.waiting;
			simple_console_text += "Processing request (unlock game) ...";
			waitMsg = "Processing request";
			SDNet.Instance.PriorityRequest(Game.ServerUrl + "key/", OnNetGameKeySubmitted, new Dictionary<string, string> { { "k", gamekeyEdit } });
		}
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region NET callbacks

	private void OnNetVersionReply(SDNet.ReturnCode code, string res)
	{
		// reply from server - version check
		if (code == SDNet.ReturnCode.OK)
		{
			simple_console_text += "Done.\n";

			// check if correct version
			if (res != Game.VER)
			{
				// if version incorrect you will want to show the player
				// some kind of message and perhaps link to the game's website
				simple_console_text += "The game must be updated.\nCurrent version: "+Game.VER+", expected version: "+res+"\n";
			}
			else
			{
				// version was fine. show the login window
				state = State.login_window;
			}
		}
		else
		{
			state = State.none;
			simple_console_text += "Failed: " + res + "\n";
		}
	}

	private void OnNetRegisterReply(SDNet.ReturnCode code, string res)
	{
		// net returned with a registration result
		if (code != SDNet.ReturnCode.OK)
		{
			simple_console_text += "\nERROR: " + res + "\n";
			state = State.reg_window;
		}
		else
		{
			simple_console_text += "Complete. You may now login.\n";
			state = State.login_window;
		}
	}

	private void OnNetRecoverPW(SDNet.ReturnCode code, string res)
	{
		if (code != SDNet.ReturnCode.OK)
		{
			simple_console_text += "\nERROR: " + res + "\n";
			state = State.login_window;
		}
		else
		{
			simple_console_text += "Complete. Check your e-mail for new password.\n";
			state = State.login_window;
		}
	}

	private void OnNetLogin(SDNet.ReturnCode code, string res)
	{
		if (code != SDNet.ReturnCode.OK)
		{
			simple_console_text += "Login failed: " + res + "\n";
			state = State.login_window;
		}
		else
		{
			state = State.inlobby;
			simple_console_text += "Done.\n";
			chat.ConnectChat();
			
			// read some settings that where saved on server
			emailNotify = Game.Instance.opt_email_notify == 1;

			// ask for latest news
			SDNet.Instance.NormalRequest(Game.ServerUrl + "news/", OnNetNews, null);

			// ask for URL to an advert to load
			SDNet.Instance.NormalRequest(Game.ServerUrl + "aimg/", OnNetAdvertURL, null);
		}
	}

	private void OnNetNews(SDNet.ReturnCode code, string res)
	{
		if (code == SDNet.ReturnCode.OK)
		{
			char[] splitter = { '|' };
			string[] msgs = res.Split(splitter);
			splitter[0] = '^';
			foreach (string m in msgs)
			{
				if (string.IsNullOrEmpty(m)) continue;
				string[] vals = m.Split(splitter);
				if (vals.Length > 1)
				{
					news_text += "[" + vals[0] + "]  " + vals[1] + "\n";
				}
			}
		}
		else news_text = "Error: Could not load news\n";
	}

	private void OnNetAdvertURL(SDNet.ReturnCode code, string res)
	{
		if (code == SDNet.ReturnCode.OK)
		{
			StartCoroutine(DownloadAdvert(res));
		}
	}

	private IEnumerator DownloadAdvert(string url)
	{
		WWW www = null;
		www = new WWW(url);
		yield return www; // wait for it download

		if (string.IsNullOrEmpty(www.error) && www.texture != null)
		{
			advert = www.texture;
		}
	}

	private void OnNetGameKeySubmitted(SDNet.ReturnCode code, string res)
	{
		state = State.inlobby;
		if (code != SDNet.ReturnCode.OK)
		{
			simple_console_text += "Failed: " + res + "\n";			
		}
		else
		{
			// res = the code of item that was unlocked
			if (res.Length == 1)
			{
				Game.Instance.owns += res;
				simple_console_text += "Done.\n";
			}
			else simple_console_text += "Failed: Unknown error\n";
		}
	}

	private void OnNetSettingsSaved(SDNet.ReturnCode code, string res)
	{
		state = State.inlobby;
		if (code != SDNet.ReturnCode.OK)
		{
			simple_console_text += "Failed: " + res + "\n";			
		}
		else
		{
			simple_console_text += "Done.\n";
		}
	}


	#endregion
	// ----------------------------------------------------------------------------------------------------------------
}
