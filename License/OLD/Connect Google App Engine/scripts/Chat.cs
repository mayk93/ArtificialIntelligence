// ====================================================================================================================
// Handles the chat, player list and friend list related stuff
// Created by Leslie Young
// http://plyoung.com or http://plyoung.wordpress.com/
// ====================================================================================================================

using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Chat
{
	public static string MAIN_CHANNEL = "public";

	public class ChatPlayer
	{
		public int id = 0;
		public string name = "";
		public int status = 3; // 0:offline, 1:online, 2:bussy, 3:unknown
		public ChatPlayer(int id, int status, string name) { this.id = id; this.status = status; this.name = name; }
	}

	public class ChannelInfo
	{
		public int id = 0;
		public string name = "";
		//public List<string> messages = new List<string>();
		public string messages = "";
	}

	public Dictionary<int, ChannelInfo> channels = new Dictionary<int, ChannelInfo>();
	public List<ChatPlayer> friends = new List<ChatPlayer>();
	public List<ChatPlayer> players = new List<ChatPlayer>();

	public string[] friendNames = null;
	public string[] playerNames = null;

	// ************************************************************************************************
	#region public

	public void UpdateNamesCache()
	{		
		friendNames = null;
		if (friends.Count > 0)
		{
			friendNames = new string[friends.Count];
			for (int i = 0; i<friends.Count; i++) friendNames[i] = friends[i].name;
		}

		playerNames = null;
		if (players.Count > 0)
		{
			playerNames = new string[players.Count];
			for (int i = 0; i < players.Count; i++)
			{
				playerNames[i] = players[i].name;
			}
		}
	}

	public ChannelInfo AddChannel(int id, string name)
	{
		if (channels.ContainsKey(id))
		{
			return channels[id];
		}

		ChannelInfo ci = new ChannelInfo();
		ci.id = id;
		ci.name = name;
		channels.Add(id, ci);

		return ci;
	}

	public ChannelInfo Channel(string channel_name)
	{
		foreach (KeyValuePair<int, ChannelInfo> kv in channels)
		{
			if (kv.Value.name == channel_name) return kv.Value;
		}
		return null;
	}

	public ChannelInfo Channel(int id)
	{
		if (channels.ContainsKey(id)) return channels[id];
		return null;
	}

	public ChannelInfo AddMessage(string channel_name, string msg)
	{
		foreach (KeyValuePair<int, ChannelInfo> kv in channels)
		{
			if (kv.Value.name == channel_name)
			{
				return AddMessage(kv.Key, msg);
			}
		}
		return null;
	}

	public ChannelInfo AddMessage(int id, string msg)
	{
		if (channels.ContainsKey(id))
		{
			//channels[id].messages.Add(msg);
			channels[id].messages += msg + "\n";
			return channels[id];
		}
		return null;
	}

	#endregion
	// ************************************************************************************************
	private static Chat _instance;
	public static Chat Instance
	{
		get
		{
			if (_instance == null) _instance = new Chat();
			return _instance;
		}
	}
	// ************************************************************************************************
}
