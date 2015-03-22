// ====================================================================================================================
// Common network class handles all network communication
// Created by Leslie Young
// http://plyoung.com or http://plyoung.wordpress.com/
// ====================================================================================================================

#define DO_DEBUG_LOG	// comment out to disable the HTML loger output

using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class SDNet : MonoBehaviour 
{
	public enum ReturnCode : int { 
		Failed = -2,				// communication with server failed
		SessionError = -1,			// player is not authenticated
		Error = 0,					// server script returned error
		OK = 1						// everything went fine according to server
	}

	public delegate void OnNetResult(ReturnCode code, string result);

	private string errmsg = ""; // error message from last network comms
	public string ErrorMsg { get { return errmsg; } }

	// handles cued network messages
	private class RequestInfo
	{
		public string url;
		public OnNetResult callback;
		public Dictionary<string, string> p;
		public int retry_on_fail = 0;
	}
	private List<RequestInfo> requests = new List<RequestInfo>();
	private List<RequestInfo> requests_lowpriority = new List<RequestInfo>();
	private RequestInfo last_request = null;
	private bool _isBussy = false;
	private float requestRetryTimer = 0f; // helper so that net waits a bit before retry so that network has chance to come back up if it failed

	// ----------------------------------------------------------------------------------------------------------------
	#region public

#if DO_DEBUG_LOG
	public void Log(string s) { SDUtil.HTMLLog(s); }
#else
	public void Log(string s){}
#endif

	public IEnumerator VersionCheck(OnNetResult callback)
	{
		_isBussy = true;

		WWW www = new WWW(Game.ServerUrl + "ver/");
		yield return www;
		errmsg = "";

		try
		{
#if DO_DEBUG_LOG
			SDUtil.HTMLLog("Version check: " + www.url + "<br>");
			if (!string.IsNullOrEmpty(www.error)) SDUtil.HTMLLog(www.error + "<br>");
			if (!string.IsNullOrEmpty(www.text)) SDUtil.HTMLLog(www.text + "<br>");
			SDUtil.HTMLLog("<hr>");
#endif

			if (!string.IsNullOrEmpty(www.error) || string.IsNullOrEmpty(www.text))
			{
				errmsg = string.IsNullOrEmpty(www.error) ? "Network communication error." : www.error;
				if (callback != null) callback(ReturnCode.Failed, errmsg);
			}
			else
			{
				if (callback != null) callback(ReturnCode.OK, www.text.Substring(1));
			}
		}
		catch (System.Exception e)
		{
			Debug.LogError(e.Message);
			Debug.LogError(e.StackTrace);
			errmsg = "Network communication error.";
			if (last_request.callback != null) last_request.callback(ReturnCode.Failed, errmsg);
		}
		finally
		{

			_isBussy = false;
		}
	}

	public IEnumerator Register(OnNetResult callback, string email, string password, string name)
	{
		_isBussy = true;

		// create params to send
		WWWForm form = new WWWForm();
		form.AddField("em", email);
		form.AddField("nm", name);
		form.AddField("pw", password);

		// let www do its thing
		WWW www = new WWW(Game.ServerUrl + "reg/", form);
		yield return www;

		try
		{
#if DO_DEBUG_LOG
			SDUtil.HTMLLog("Register: " + www.url + "[em=" + email + ", nm=" + name + ", pw=" + password + "]<br>");
			if (!string.IsNullOrEmpty(www.error)) SDUtil.HTMLLog(www.error + "<br>");
			if (!string.IsNullOrEmpty(www.text)) SDUtil.HTMLLog(www.text + "<br>");
			SDUtil.HTMLLog("<hr>");
#endif

			// handle the data from www
			if (!string.IsNullOrEmpty(www.error) || string.IsNullOrEmpty(www.text))
			{
				errmsg = string.IsNullOrEmpty(www.error) ? "Network communication error." : www.error;
				if (callback != null) callback(ReturnCode.Failed, errmsg);
			}
			else
			{
				errmsg = "Network communication error.";
				if (callback != null)
				{
					if (www.text[0] == '1')
					{
						callback(ReturnCode.OK, null);
					}
					else if (www.text[0] == '0' || www.text[0] == '!')
					{
						errmsg = "Could not register your new account.";
						if (www.text.Length > 1) errmsg = www.text.Substring(1);
						callback(ReturnCode.Error, errmsg);
					}
					else
					{
						// this should only happen during development since there was an unexpected 
						// value at [0], not 0 or 1 as expected, so probably some server script error
						errmsg = "Network communication error.";
						callback(ReturnCode.Failed, errmsg);
					}
				}
			}
		}
		catch (System.Exception e)
		{
			Debug.LogError(e.Message);
			Debug.LogError(e.StackTrace);
			errmsg = "Network communication error.";
			if (last_request.callback != null) last_request.callback(ReturnCode.Failed, errmsg);
		}
		finally
		{
			_isBussy = false;
		}
	}

	public IEnumerator RecoverPW(OnNetResult callback, string email)
	{
		_isBussy = true;

		// create params to send
		WWWForm form = new WWWForm();
		form.AddField("em", email);

		// let www do its thing
		WWW www = new WWW(Game.ServerUrl + "rpw/", form);
		yield return www;

		try
		{
#if DO_DEBUG_LOG
			SDUtil.HTMLLog("Recover PW: " + www.url + "[em=" + email + "]<br>");
			if (!string.IsNullOrEmpty(www.error)) SDUtil.HTMLLog(www.error + "<br>");
			if (!string.IsNullOrEmpty(www.text)) SDUtil.HTMLLog(www.text + "<br>");
			SDUtil.HTMLLog("<hr>");
#endif

			// handle the data from www
			if (!string.IsNullOrEmpty(www.error) || string.IsNullOrEmpty(www.text))
			{
				errmsg = string.IsNullOrEmpty(www.error) ? "Network communication error." : www.error; 
				if (callback != null) callback(ReturnCode.Failed, errmsg);
			}
			else
			{
				errmsg = "Network communication error.";
				if (callback != null)
				{
					if (www.text[0] == '1')
					{
						callback(ReturnCode.OK, null);
					}
					else if (www.text[0] == '0' || www.text[0] == '!')
					{
						errmsg = "Could not complete your request.";
						if (www.text.Length > 1) errmsg = www.text.Substring(1);
						callback(ReturnCode.Error, errmsg);
					}
					else
					{
						// this should only happen during development since there was an unexpected 
						// value at [0], not 0 or 1 as expected, so probably some script error
						errmsg = "Network communication error.";
						callback(ReturnCode.Failed, errmsg);
					}
				}
			}
		}
		catch (System.Exception e)
		{
			Debug.LogError(e.Message);
			Debug.LogError(e.StackTrace);
			errmsg = "Network communication error.";
			if (last_request.callback != null) last_request.callback(ReturnCode.Failed, errmsg);
		}
		finally
		{
			_isBussy = false;
		}
	}

	public IEnumerator Login(OnNetResult callback, string nm, string pw)
	{
		_isBussy = true;
		string session_cookie = null;

		// create params to send
		WWWForm form = new WWWForm();
		form.AddField("nm", nm);
		form.AddField("pw", pw);

		// let www do its thing
		WWW www = new WWW(Game.ServerUrl + "login/", form);
		yield return www;

		try
		{
#if DO_DEBUG_LOG
			SDUtil.HTMLLog("LOGIN: " + www.url + "[nm=" + nm + ", pw=" + pw + "]<br>");
			if (!string.IsNullOrEmpty(www.error)) SDUtil.HTMLLog(www.error + "<br>");
			if (!string.IsNullOrEmpty(www.text)) SDUtil.HTMLLog(www.text + "<br>");
			SDUtil.HTMLLog("<hr>");
			foreach (KeyValuePair<string, string> kv in www.responseHeaders)
			{
				SDUtil.HTMLLog(kv.Key + " => " + kv.Value + "<br>");
			}
			SDUtil.HTMLLog("<hr>");
#endif


			// handle the data from www
			if (!string.IsNullOrEmpty(www.error) || string.IsNullOrEmpty(www.text))
			{
				errmsg = string.IsNullOrEmpty(www.error) ? "Network communication error." : www.error; 
				if (callback != null) callback(ReturnCode.Failed, errmsg);
			}
			else
			{
				errmsg = "Network communication error.";

				if (www.text[0] == '1')
				{
					try
					{
						string[] v = www.text.Split(new char[] { '^' });

						session_cookie = v[0].Substring(1);		// session id (in case i could not get it from headers)				
						Game.Instance.name = v[1];				// extract the public name of player
						Game.Instance.owns = v[2];				// string that tells which parts of game the player owns
						Game.Instance.opt_email_notify = SDUtil.ParseInt(v[3], 0); // setting that where saved on server

						Game.Instance.ClearSessionCookie();
						UpdateCookie(www);

						// just incase the cookies could not be found in the header
						//SDUtil.HTMLLog("Cookie: " + session_cookie + "<hr>");
						if (!Game.Instance.SessionCookieIsSet && !string.IsNullOrEmpty(session_cookie))
						{
							Game.Instance.SetSessionCookie(session_cookie);
						}
					}
					catch
					{
						// this should only possibly happen during development
						Debug.LogError("This should not happen");
						if (callback != null) callback(ReturnCode.Failed, "Network communication error.");
					}
				}

				if (callback != null)
				{
					if (www.text[0] == '1' && Game.Instance.SessionCookieIsSet)
					{
						callback(ReturnCode.OK, "Login ok");
					}
					else if (www.text[0] == '0' || www.text[0] == '!' || !Game.Instance.SessionCookieIsSet)
					{
						errmsg = "Invalid login name or password.";
						if (!Game.Instance.SessionCookieIsSet) errmsg = "System error. Could not create session.";
						callback(ReturnCode.Error, errmsg);
					}
					else
					{
						// this should only happen during development since there was an unexpected 
						// value at [0], not 0 or 1 as expected, so probably some script error
						errmsg = "Network communication error.";
						callback(ReturnCode.Failed, errmsg);
					}
				}
			}

#if DO_DEBUG_LOG
			SDUtil.HTMLLog("Cookie: " + Game.Instance.GetSessionCookie() + "<hr>");
#endif
		}
		catch (System.Exception e)
		{
			Debug.LogError(e.Message);
			Debug.LogError(e.StackTrace);
			errmsg = "Network communication error.";
			if (last_request.callback != null) last_request.callback(ReturnCode.Failed, errmsg);
		}
		finally
		{
			_isBussy = false;
		}
	}

	public IEnumerator Logout()
	{
		WWWForm form = new WWWForm();
		form.AddField("gi", "bm"); // must have data to use WWW() below
		WWW www = new WWW(Game.ServerUrl + "logout/", form.data, Game.Instance.SessionCookie);
		yield return www;
	}

	private void UpdateCookie(WWW www)
	{
		// check if session cookie was send, if not, well, no use to continue then					
		if (www.responseHeaders.ContainsKey("SET-COOKIE"))
		{
			Game.Instance.ClearSessionCookie();
			// extract the session identifier cookie and save it. the cookie will 
			// be named, "auth"
			char[] splitter = { ';' };
			string[] v = www.responseHeaders["SET-COOKIE"].Split(splitter);
			foreach (string s in v)
			{
				if (string.IsNullOrEmpty(s)) continue;
				if (s.Substring(0, 4).ToLower().Equals("auth"))
				{
					Game.Instance.SetSessionCookie(s);
					break;
				}
			}
		}
	}

	// PriorityRequest and NormalRequest are the two main ways of sending a message to the server.
	// specify the url to contact, a callback to call when server replied and a dict of fields
	// and values to send

	public void PriorityRequest(string url, OnNetResult callback, Dictionary<string, string> p)
	{
		// create important request
		CreateRequest(false, url, callback, p);
	}

	public void NormalRequest(string url, OnNetResult callback, Dictionary<string, string> p)
	{
		// create low priority request
		CreateRequest(true, url, callback, p);
	}

	private void CreateRequest(bool low_priority, string url, OnNetResult callback, Dictionary<string, string> p)
	{
		RequestInfo r = new RequestInfo();
		r.url = url;
		r.callback = callback;
		r.p = p;
		r.retry_on_fail = (low_priority ? 0 : 2); // priority requests should always retry
		if (low_priority) requests_lowpriority.Add(r);
		else requests.Add(r);
	}

	public void ClearAllRequests()
	{
		requests_lowpriority.Clear();
		requests.Clear();
	}

	public void ClearRequestWithCallback(OnNetResult callback, bool from_low_priority_list)
	{
		List<RequestInfo> remove = new List<RequestInfo>();
		if (from_low_priority_list)
		{
			foreach (RequestInfo r in requests_lowpriority)
			{
				if (r.callback == callback) remove.Add(r);
			}
			foreach (RequestInfo r in remove) requests_lowpriority.Remove(r);
			remove.Clear();
		}
		else
		{
			foreach (RequestInfo r in requests)
			{
				if (r.callback == callback) remove.Add(r);
			}
			foreach (RequestInfo r in remove) requests.Remove(r);
			remove.Clear();
		}
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region internal

	void Start()
	{
		_isBussy = false;
	}

	void OnApplicationQuit()
	{
		if (Game.Instance.SessionCookieIsSet && !string.IsNullOrEmpty(Game.ServerUrl))
		{
			StartCoroutine(Logout());
		}
	}

	void OnDestroy()
	{
		if (_instance != null)
		{
			_instance.ClearAllRequests();
			_instance = null;
		}
	}

	void LateUpdate()
	{
		if (!_isBussy)
		{
			if (last_request != null)
			{
				requestRetryTimer -= Time.deltaTime;
				if (requestRetryTimer <= 0f)
				{
					// just make a call to _perform, the lists will be ignored and "last_request" used as is
					StartCoroutine(_Perform(false));
				}
			}
			else
			{
				if (requests.Count > 0) StartCoroutine(_Perform(false));
				else if (requests_lowpriority.Count > 0) StartCoroutine(_Perform(true));
			}
		}
	}

	private IEnumerator _Perform(bool from_low_priority_lit)
	{
		_isBussy = true;
		errmsg = "";

		if (last_request == null)
		{
			// grab the first request in the list
			if (from_low_priority_lit)
			{
				last_request = requests_lowpriority[0];
				requests_lowpriority.RemoveAt(0);
			}
			else
			{
				last_request = requests[0];
				requests.RemoveAt(0);
			}
		}
		else
		{
			Debug.Log("Retry: " + last_request.retry_on_fail + " => " + last_request.url);
		}

		// create params to send
		WWWForm form = new WWWForm();

		bool nofields = true;
		if (last_request.p != null)
		{
			foreach (KeyValuePair<string, string> kv in last_request.p) 
			{
				nofields = false;
				form.AddField(kv.Key, kv.Value);
			}
		}

		if (nofields)
		{
			// always need data, else WWW() will throw error below,
			// so just add this misc field incase there are no other data
			form.AddField("x", "0");
		}

		// let www do its thing
		WWW www = (Application.isWebPlayer ? new WWW(last_request.url, form.data) : new WWW(last_request.url, form.data, Game.Instance.SessionCookie));
		yield return www;

		try
		{
#if DO_DEBUG_LOG
			SDUtil.HTMLLog(www.url + "<br>");
			if (last_request.p != null)
			{
				foreach (KeyValuePair<string, string> kv in last_request.p) SDUtil.HTMLLog(" ::: " + kv.Key + " =" + kv.Value + "<br>");
			}
			if (!string.IsNullOrEmpty(www.error)) SDUtil.HTMLLog(www.error + "<br>");
			if (!string.IsNullOrEmpty(www.text)) SDUtil.HTMLLog(www.text + "<br>");
			SDUtil.HTMLLog("<hr>");
#endif

			// handle the data from www
			if (!string.IsNullOrEmpty(www.error) || string.IsNullOrEmpty(www.text))
			{
				if (last_request.retry_on_fail <= 0)
				{	// only accept failure if this request dont have retries left
					errmsg = string.IsNullOrEmpty(www.error) ? "Network communication error." : www.error; 
					if (last_request.callback != null) last_request.callback(ReturnCode.Failed, errmsg);
				}
			}
			else
			{
				UpdateCookie(www);
				last_request.retry_on_fail = 0; // to be sure it wont retry in next update call since it "succeeded"

				if (last_request.callback != null)
				{
					if (www.text[0] == '1')
					{
						string s = (www.text.Length > 1 ? www.text.Substring(1) : "");
						last_request.callback(ReturnCode.OK, s);
					}
					else if (www.text[0] == '0')
					{
						errmsg = (www.text.Length > 1 ? www.text.Substring(1) : "");
						last_request.callback(ReturnCode.Error, errmsg);
					}
					else if (www.text[0] == '!')
					{
						errmsg = "You are not authenticated or the server has gone off-line. Please restart the game.";
						last_request.callback(ReturnCode.Error, errmsg);
					}
					else
					{
						// this should only happen during development since there was an unexpected 
						// value at [0], not 0 or 1 as expected, so probably some server script error
						// NOTE: Can also happen if player is not loged-in/authorised (will receive a '!' at [0])
						//if (Application.isEditor) Util.HTMLLog(www.text);
						Debug.LogError(www.text);
						errmsg = "Network communication error.";
						Debug.LogError("Failed: URL = " + last_request.url);
						last_request.callback(ReturnCode.Failed, errmsg);
					}
				}

			}
		}
		catch (System.Exception e)
		{
			Debug.LogError(e.Message);
			Debug.LogError(e.StackTrace);
			if (last_request.retry_on_fail <= 0)
			{	// only accept failure if this request dont have retries left
				errmsg = "Network communication error.";
				Debug.LogError("Failed: " + www.error + ", URL = " + last_request.url);
				if (last_request.callback != null) last_request.callback(ReturnCode.Failed, errmsg);
			}
		}
		finally
		{
			// check if the request should retry or if done with it now
			if (last_request.retry_on_fail > 0)
			{
				last_request.retry_on_fail--;
				requestRetryTimer = 100f; // reset timer
			}
			else last_request = null;

			_isBussy = false;
		}
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	private static SDNet _instance;
	public static SDNet Instance
	{
		get
		{
			if (_instance == null)
			{
				GameObject go = GameObject.Find("SDNET");
				if (go)
				{
					_instance = go.GetComponent<SDNet>();
				}
				else
				{
					go = new GameObject("SDNET");
					_instance = go.AddComponent<SDNet>();
				}
			}
			return _instance;
		}
	}
	// ----------------------------------------------------------------------------------------------------------------
}
