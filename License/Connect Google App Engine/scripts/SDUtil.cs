// ====================================================================================================================
// Common Utils class
// Created by Leslie Young
// http://plyoung.com or http://plyoung.wordpress.com/
// ====================================================================================================================

using UnityEngine;
using System.Collections;
using System.IO;

public class SDUtil
{

	// ----------------------------------------------------------------------------------------------------------------
	#region conversion

	public static int ParseInt(string s, int default_val)
	{
		int ret = default_val;
		try { ret = int.Parse(s); } catch { ret = default_val; }
		return ret;
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	#region logging

	public string _debug_log = string.Empty;
	public static void HTMLLog(string msg)
	{
		SDUtil.Instance._debug_log += msg;
	}

	public static void DumpHTMLLog()
	{	// saves an html page and call browser to open it, usefull when having
		// to debug data being send from a webserver in HTML format ;)
		try
		{
			string path = Application.persistentDataPath + "/log.html";
			using (FileStream fs = new FileStream(path, FileMode.Create))
			{
				using (StreamWriter sw = new StreamWriter(fs))
				{
					sw.Write(SDUtil.Instance._debug_log);
				}
			}
			Application.OpenURL(path);
		}
		catch { Debug.LogError("Failed to write HTML debug file."); }
		SDUtil.Instance._debug_log = string.Empty;
	}

	#endregion
	// ----------------------------------------------------------------------------------------------------------------
	private static SDUtil _instance;
	public static SDUtil Instance
	{
		get
		{
			if (_instance == null) _instance = new SDUtil();
			return _instance;
		}
	}
	// ----------------------------------------------------------------------------------------------------------------
}
