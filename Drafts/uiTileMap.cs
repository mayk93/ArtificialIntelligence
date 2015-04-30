using UnityEngine.UI;
using UnityEngine;
using System.Collections;

public class InstantiateMap : MonoBehaviour
{
	public Sprite plainsImage;
	public Sprite marshImage;
	public Sprite hillImage;
	public Sprite mountainImage;

	/* --- --- --- */

	private GameObject UIscreen;
	private GameObject map;

	private int numberOfTiles = 40;
	private int numberOfTilesRow = 4;
	private int numberOfTilesColumn = 10;

	private float tileWidth = 0.0f;
	private float tileHeight = 0.0f;

	// Use this for initialization
	void Start ()
	{
		CalculateTileSize ();
		CreateScreen ();
		CreateMap ();
		AddMapImage ();
	}

	void CalculateTileSize()
	{
		float screenWidth = Screen.width;
		float screenHeight = Screen.height;
		tileWidth = screenWidth/numberOfTilesRow;
		tileHeight = screenHeight / numberOfTilesColumn;
	}

	void CreateScreen()
	{
		UIscreen  = new GameObject("Screen", typeof(RectTransform));
		UIscreen.AddComponent<Canvas>();
		UIscreen.AddComponent<GraphicRaycaster>();
	}

	void CreateMap()
	{
		for(int horizontalIndex = 0; horizontalIndex <= numberOfTilesRow; horizontalIndex++)
		{
			for(int verticalIndex = 0; verticalIndex <= numberOfTilesColumn; verticalIndex++)
			{
				map = new GameObject("Tile", typeof(RectTransform));
				map.AddComponent<CanvasRenderer>();
				map.AddComponent<Image>();
				RectTransform mapRectTransform = (RectTransform)map.transform;

				mapRectTransform.anchorMax = new Vector2(0,0);
				mapRectTransform.anchorMin = new Vector2(0,0);
				mapRectTransform.anchoredPosition = new Vector2(0,0);
				mapRectTransform.pivot = new Vector2(0,0);

				//mapRectTransform.position = new Vector2(horizontalIndex*tileWidth + 1,verticalIndex*tileHeight + 1);
				mapRectTransform.sizeDelta = new Vector2(tileWidth, tileHeight);
				mapRectTransform.sizeDelta = new Vector2(tileWidth, tileHeight);
				mapRectTransform.sizeDelta = new Vector2(1, 1);
				map.transform.parent = UIscreen.transform;
				AddMapImage();
			}
		}
	}

	void AddMapImage()
	{
		Sprite[] mapSprites = new Sprite[4];
		mapSprites[0] = plainsImage;
		mapSprites[1] = marshImage;
		mapSprites[2] = hillImage;
		mapSprites[3] = mountainImage;
		int terrainType = Random.Range (0, mapSprites.Length);
		if( mapSprites[terrainType] != null )
		{
			Image mapImageHolder = (Image)map.GetComponent<Image>();
			mapImageHolder.sprite = mapSprites[terrainType];
		}
	}
}
