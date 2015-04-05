// ====================================================================================================================
// Game globals
// Created by Leslie Young
// http://plyoung.com or http://plyoung.wordpress.com/
// ====================================================================================================================

using UnityEngine;
using System.Collections;

public class Game
{
	// ----------------------------------------------------------------------------------------------------------------
	#region defines

	// the build version to compare with server during login to check if this client is up to date (MUST BE SAME AS ON SERVER)
	public static string VER = "000";
	
	// main url of the game server (change this to your test machine IP or GAE url - http://myapp.appspot.com/)
	// this is how it might look when testing on your localhost 
	//public static string ServerUrl = "http://192.168.1.78:8081/";

	// This is a test server on GAE and set to a "free" subscription. Besides that, it will not know how to talk to 
	// any changes you make. so dont depend on it! Change "unitygae" to the name of your app!!
	public static string ServerUrl = "http://unitygae.appspot.com/";

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region public

	// Player Profile
	public string nm = "";			// login name
	public string pw = "";			// password
	public string name = "";		// screen name
	public string owns;			    // tells if player owns free or base game and any expansions. I am working with a string here since
									// it will contain characters to indicate whqat the player owns, like "1" for full game, "B" for some DLC, etc
									// you could obvioulsy extract the characters after "owns" was set and set bools or inst or whatever is
									// quicker to access depending on your situation
	private Hashtable session_ident = new Hashtable();	// will be set to some session id after login

	public int opt_email_notify = 0; // sample setting saved on server side

	public static float LOBBY_REFRESH_TIMEOUTS = 10f;			// seconds to wait before player may use various refresh buttons in lobby
	public static float LOBBY_AUTO_REFRESH_TIMEOUTS = 60f;		// seconds to wait before auto refresh runs
	public static float FRIENDS_REFRESH_TIMEOUTS = 120f;		// x second refresh of friends list

	public static float CHAT_MSG_REFRESH_TIMEOUTS_START = 20f;	// x second refresh of chat messages
	public static float CHAT_MSG_REFRESH_TIMEOUTS_MIN = 12f;	// x second refresh of chat messages
	public static float CHAT_MSG_REFRESH_TIMEOUTS_MAX = 45f;	// x second refresh of chat messages

	public static float GAME_REFRESH_TIMEOUTS_MIN = 10f;		// game refresh/query timeout
	public static float GAME_REFRESH_TIMEOUTS_MAX = 30f;		// game refresh/query timeout

	public float ChatMsgRefreshTimeout = CHAT_MSG_REFRESH_TIMEOUTS_START;
	public float GameRefreshTimeout = GAME_REFRESH_TIMEOUTS_MIN;

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region pub

	public void Update_ChatMsgRefreshTimeout(bool inc)
	{
		if (inc) ChatMsgRefreshTimeout++;	// wait a bit longer before checking again if not getting any msgs
		else
		{
			if (ChatMsgRefreshTimeout > CHAT_MSG_REFRESH_TIMEOUTS_MIN) ChatMsgRefreshTimeout = CHAT_MSG_REFRESH_TIMEOUTS_MIN;
			else ChatMsgRefreshTimeout--;	// check again earlier if receiving msgs
		}
		if (ChatMsgRefreshTimeout < CHAT_MSG_REFRESH_TIMEOUTS_MIN) ChatMsgRefreshTimeout = CHAT_MSG_REFRESH_TIMEOUTS_MIN;
		if (ChatMsgRefreshTimeout > CHAT_MSG_REFRESH_TIMEOUTS_MAX) ChatMsgRefreshTimeout = CHAT_MSG_REFRESH_TIMEOUTS_MAX;
	}

	public void Update_GameRefreshTimeout(bool inc)
	{
		if (inc) GameRefreshTimeout++;
		else GameRefreshTimeout = GAME_REFRESH_TIMEOUTS_MIN;
		if (GameRefreshTimeout < CHAT_MSG_REFRESH_TIMEOUTS_MIN) GameRefreshTimeout = GAME_REFRESH_TIMEOUTS_MIN;
		if (GameRefreshTimeout > CHAT_MSG_REFRESH_TIMEOUTS_MAX) GameRefreshTimeout = GAME_REFRESH_TIMEOUTS_MAX;
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region session related

	public void ClearSessionCookie()
	{
		session_ident["Cookie"] = "";
	}

	public void SetSessionCookie(string s)
	{
		session_ident["Cookie"] = s;
	}

	public Hashtable SessionCookie
	{
		get { return session_ident; }
	}

	public string GetSessionCookie()
	{
		return session_ident["Cookie"] as string;
	}

	public bool SessionCookieIsSet
	{
		get 
		{
			if (session_ident["Cookie"] != null)
			{
				return (session_ident["Cookie"] as string).Length > 0;
			}
			return false;
		}
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	private static Game _instance;
	public static Game Instance
	{
		get
		{
			if (_instance == null) _instance = new Game();
			return _instance;
		}
	}
	// ----------------------------------------------------------------------------------------------------------------
}
