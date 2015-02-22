#include <gtk/gtk.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <unistd.h>
#include <X11/Xlib.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

//static int *hasBeenAccepted;
int hasBeenAccepted = 0;

    /* IMPORTANT!!! */
    
        /*
        The matrix must be change to a 3D matrix in order to
        record all possible transitions.
        
        See example aadbe, where we can transition from
        state 1 with BOTH "b" and "e" to 3. Currently, only "e"
        is recorded as facilitating the transition.
        
        Please fix immedietly!
        */
    
    /* IMPORTANT!!! */

void NFA(int numberOfStates,vector<vector<string> > transitionMatrix,vector<long int> finalStates,string alphabet, string wordToCheck, int currentState, string currentLetter, int currentLetterIndex, pid_t mainProcessPID)
{
    if(currentLetterIndex < wordToCheck.length())
    {
        /*
        cout<<"====="<<endl;
        cout<<"Current State: "<<currentState<<endl;
        cout<<"Current Letter: "<<currentLetter<<endl;
        cout<<"Main Process Pid: "<<mainProcessPID<<endl;
        cout<<"Possible next states: ";
        */
        vector<string> possibleTransitions = transitionMatrix.at(currentState);
        int possibleNextState = 0;
        
        vector<int> possibleNextStatesVector;
        
        for(vector<string>::iterator itStr = possibleTransitions.begin(); itStr != possibleTransitions.end(); ++itStr)
        {
            string transitionSymbol = *itStr;
            if(currentLetter == transitionSymbol)
            {
                //cout<<possibleNextState<<" ";
                possibleNextStatesVector.push_back(possibleNextState);
            }
            possibleNextState = possibleNextState + 1;
        }
        //cout<<endl;
        //cout<<"====="<<endl<<endl;
        
        if( !possibleNextStatesVector.empty() )
        {
            for(vector<int>::iterator psi = possibleNextStatesVector.begin(); psi != possibleNextStatesVector.end(); ++psi)
            {
              string currentLetter;
              stringstream ss;
              ss << wordToCheck[currentLetterIndex+1];
              ss >> currentLetter;
              
              NFA(numberOfStates,transitionMatrix,finalStates,alphabet,wordToCheck,*psi,currentLetter,currentLetterIndex+1,mainProcessPID);
            }
        }
        else
        {
            //cout<<"Return 0."<<endl;
            return;
        }
    }
    else
    {
        //cout<<"State at ending: "<<currentState<<endl;
        if(std::find(finalStates.begin(), finalStates.end(), currentState) != finalStates.end())
        {
            hasBeenAccepted = 1;
            //cout<<"Accepted."<<endl;
        }
        //cout<<"Return 1."<<endl;
        return;
    }
}

/*
void NFA(int numberOfStates,vector<vector<string> > transitionMatrix,vector<long int> finalStates,string alphabet, string wordToCheck, int currentState, int currentLetterIndex, pid_t mainProcessPID)
{
    if(std::find(finalStates.begin(), finalStates.end(), currentState) != finalStates.end() && currentLetterIndex >= wordToCheck.size()-1)
    {
        //*hasBeenAccepted = 1;
        cout<<"Word Accepted 0"<<endl;
        if(getpid() != mainProcessPID)
        {
            cout<<"XYZ"<<endl;
            kill(getpid(), SIGKILL);
            //exit(EXIT_SUCCESS);
        }        
    }

    //cout<<"====="<<endl;
    //cout<<currentState<<" "<<currentLetterIndex<<endl;
    
    pid_t the_pid;
    string currentLetter;
    if(currentLetterIndex < wordToCheck.size())
    {
        stringstream ss;
        ss << wordToCheck[currentLetterIndex];
        
        ss >> currentLetter;
        
        vector<string> possibleTransitions = transitionMatrix.at(currentState);
        
        //cout<<"Current Letter: "<<currentLetter<<endl;    
        //cout<<"Current Possible Transitions: "<<endl;
        
        for(vector<string>::iterator itStr = possibleTransitions.begin(); itStr != possibleTransitions.end(); ++itStr)
        {
            //cout<<*itStr<<" ";
        }
        //cout<<endl<<"====="<<endl<<endl;
        
        for(int possibleNextState = 0; possibleNextState < possibleTransitions.size(); possibleNextState++)
        {
            if(possibleTransitions[possibleNextState] == currentLetter)
            {
                the_pid = fork();
                if(the_pid == 0) //Child
                {
                    currentState = possibleNextState;
                    currentLetterIndex = currentLetterIndex + 1;
                    NFA(numberOfStates,transitionMatrix,finalStates,alphabet,wordToCheck,currentState,currentLetterIndex,mainProcessPID);
                }
                else //Father
                {
                    size_t isHere = alphabet.find(currentLetter);
                    
                    //munmap(hasBeenAccepted, sizeof *hasBeenAccepted);
                    
                    if((hasBeenAccepted == 0)&&(( (currentLetterIndex >= wordToCheck.size()) && (!(std::find(finalStates.begin(), finalStates.end(), currentState) != finalStates.end())) ) || isHere==std::string::npos))
                    {
                        cout<<"Word Rejected 0"<<endl;
                        if(getpid() != mainProcessPID)
                        {
                            kill(the_pid, SIGKILL);
                        }
                    }
                    else
                    {
                        if(std::find(finalStates.begin(), finalStates.end(), currentState) != finalStates.end())
                        {
                            //*hasBeenAccepted = 1;
                            cout<<"Word Accepted 1"<<endl;
                            if(getpid() != mainProcessPID)
                            {
                                kill(the_pid, SIGKILL);
                            }
                        }
                    }
                }
            }
        }
    }
    else
    {
        size_t isHere = alphabet.find(currentLetter);
        
        //munmap(hasBeenAccepted, sizeof *hasBeenAccepted);
        
        if((hasBeenAccepted == 0) && (( (currentLetterIndex >= wordToCheck.size()) && (!(std::find(finalStates.begin(), finalStates.end(), currentState) != finalStates.end())) ) || isHere==std::string::npos))
        {
            cout<<"Word Rejected 1"<<endl;
            if(getpid() != mainProcessPID)
            {
                kill(the_pid, SIGKILL);
            }
        }
        else
        {
            if(std::find(finalStates.begin(), finalStates.end(), currentState) != finalStates.end())
            {
                cout<<"Word Accepted 2"<<endl;
                if(getpid() != mainProcessPID)
                {
                    kill(the_pid, SIGKILL);
                }
            }
        }    
    }
}
*/

int readTransition(string path, int numberOfStates, string finalStatesRaw,string alphabet, string wordToCheck)
{
    string defaultSymbol = "#";
    vector< vector<string> > transitionMatrix(numberOfStates,vector<string>(numberOfStates,defaultSymbol));
    string line;
    
    ifstream myfile (path.c_str());
    
    if (myfile.is_open())
    {
      vector<string> tokens;
      while ( getline (myfile,line) )
      {
          string str(line);
          string buf;
          stringstream ss(str); 
          while (ss >> buf)
          {
              tokens.push_back(buf);             
          }
      }
      
      for(int ix = 0; ix < tokens.size()-3; ix = ix + 3)
      {
          char* pEnd;
          long int currentState = strtol (tokens.at(ix).c_str(),&pEnd,10);
          string symbol = tokens.at(ix+1);
          long int nextState = strtol (tokens.at(ix+2).c_str(),&pEnd,10);
          
          for(long int i = 0; i < numberOfStates; i++)
	      {
		      for(long int j = 0; j < numberOfStates; j++)
		      {
		          if(i == currentState && j == nextState)
		          {
		              transitionMatrix[i][j] = symbol;
		          }
		      }
	      }
      }
      myfile.close();
      
      vector<string> tokensX;
      string strX(finalStatesRaw);
      string bufX;
      stringstream ssX(strX); 
      while (ssX >> bufX)
      {
          tokensX.push_back(bufX);             
      }
    
      vector<long int> finalStates;
      for(vector<string>::iterator sit = tokensX.begin(); sit != tokensX.end(); ++sit)
      {
          char* pEnd;
          string possibleFinalStateString(*sit);
          long int possibleFinalState = strtol (possibleFinalStateString.c_str(),&pEnd,10);
          finalStates.push_back(possibleFinalState);
      }         
      
      //int numberOfStates,vector<vector<string> > transitionMatrix,vector<long int> finalStates,string alphabet, string wordToCheck, int currentState, int currentLetterIndex
      pid_t mainProcessPID = getpid();
      
      //NFA(numberOfStates,transitionMatrix,finalStates,alphabet,wordToCheck,0,0,mainProcessPID);
      string currentLetter;
      stringstream ss;
      ss << wordToCheck[0];
      ss >> currentLetter;
      
      /*
      for(int i = 0; i<numberOfStates; i++)
      {
        for(int j = 0; j<numberOfStates; j++)
        {
            cout<<transitionMatrix[i][j]<<" ";
        }
        cout<<endl;
      }
      */
      
      NFA(numberOfStates,transitionMatrix,finalStates,alphabet,wordToCheck,0,currentLetter,0,mainProcessPID);
      
      if(hasBeenAccepted == 0)
      {
        cout<<"Rejected."<<endl;
      }
      else
      {
        cout<<"Accepted."<<endl;
      }
      
      return 0;
    }
    else
    {
        return -1;
    }  

  return -1;
}

static void onClick(GtkWidget **entry, GtkWidget *widget)
{    
  GtkWidget *entry_ptr_a = entry[0];
  GtkWidget *entry_ptr_s = entry[1];
  GtkWidget *entry_ptr_t = entry[2];
  GtkWidget *entry_ptr_v = entry[3];
  GtkWidget *entry_ptr_r = entry[4];

  const gchar *entryStatesQ_NumberOfStates, 
               *entrySymbolsE_Alphabet,
               *entryTransitionTableD_Path, 
               *entryFinalStatesF_FS, 
               *entry_WordToCheck;


  entryStatesQ_NumberOfStates = gtk_entry_get_text(GTK_ENTRY (entry_ptr_a));
  entrySymbolsE_Alphabet = gtk_entry_get_text(GTK_ENTRY (entry_ptr_s));
  entryTransitionTableD_Path = gtk_entry_get_text(GTK_ENTRY (entry_ptr_t));
  entryFinalStatesF_FS = gtk_entry_get_text(GTK_ENTRY (entry_ptr_v));
  entry_WordToCheck = gtk_entry_get_text(GTK_ENTRY (entry_ptr_r));
    
  char* pEnd;
  long int numberOfStates = -1;  
  
  numberOfStates = strtol (entryStatesQ_NumberOfStates, &pEnd, 10); 
  string alphabet(entrySymbolsE_Alphabet);
  string pathToFile(entryTransitionTableD_Path);
  string finalStates(entryFinalStatesF_FS);
  string toCheck(entry_WordToCheck);
  
  readTransition(pathToFile,numberOfStates,finalStates,alphabet,toCheck);
}

int main(int argc, char* argv[])
{
    //hasBeenAccepted = (int*)mmap(NULL, sizeof *hasBeenAccepted, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    //*hasBeenAccepted = 0;

    //Variables
    const char* titleText      = "Nondeterministic Finite Automaton";
    const char* statesText     = "Enter number of states";
    const char* symbolsText    = "Enter Symbols";
    const char* transitionText = "Enter path to transition table";
    const char* finalText      = "Enter final states";
    
    //Initialize Gtk
    XInitThreads();
    gtk_init(&argc,&argv);
    
    //Widgets
    GtkWidget* window;
    GtkWidget* label;
    GtkWidget* entry;
    GtkWidget* button;
    GtkWidget* frame;
    
    //NFA Input
    GtkWidget* labelStatesQ;
    GtkWidget* entryStatesQ;
    GtkWidget* labelSymbolsE;
    GtkWidget* entrySymbolsE;
    GtkWidget* labelTransitionTableD;
    GtkWidget* entryTransitionTableD;
    GtkWidget* labelFinalStatesF;
    GtkWidget* entryFinalStatesF;    
    
    //Widgets Functionality:
        //Initialize Widgets
    window   = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    label    = gtk_label_new("");
    entry    = gtk_entry_new();
    button   = gtk_button_new_with_label("Test Word");
    
    labelStatesQ          = gtk_label_new("");
    labelSymbolsE         = gtk_label_new("");
    labelTransitionTableD = gtk_label_new("");
    labelFinalStatesF     = gtk_label_new("");
    
    entryStatesQ          = gtk_entry_new();
    entrySymbolsE         = gtk_entry_new();
    entryTransitionTableD = gtk_entry_new();
    entryFinalStatesF     = gtk_entry_new();
    
    //GtkWidget **entryArray;
    GtkWidget* entryArray[5];
    //entryArray = malloc(4 * sizeof(GtkWidget));
    entryArray[0] = entryStatesQ;
    entryArray[1] = entrySymbolsE;
    entryArray[2] = entryTransitionTableD;
    entryArray[3] = entryFinalStatesF;
    entryArray[4] = entry;
    
    frame    = gtk_fixed_new();
        //Functionality
    g_signal_connect(window,"delete-event",G_CALLBACK(gtk_main_quit),NULL);
    //g_signal_connect(button,"clicked",G_CALLBACK(onClick),NULL);
    g_signal_connect_swapped (button, "clicked", G_CALLBACK (onClick), entryArray);
    gtk_window_set_title(GTK_WINDOW(window),titleText);
    
    // Label Texts
    gtk_label_set_text(GTK_LABEL(label),titleText);
    gtk_label_set_text(GTK_LABEL(labelStatesQ),statesText);
    gtk_label_set_text(GTK_LABEL(labelSymbolsE),symbolsText);
    gtk_label_set_text(GTK_LABEL(labelTransitionTableD),transitionText);
    gtk_label_set_text(GTK_LABEL(labelFinalStatesF),finalText);
    
    gtk_window_set_default_size(GTK_WINDOW(window), 250, 500);
    gtk_widget_set_size_request(button, 100, 25);
    gtk_container_add(GTK_CONTAINER(window), frame);
    
    //States
    gtk_fixed_put(GTK_FIXED(frame), labelStatesQ, 10, 25);
    gtk_fixed_put(GTK_FIXED(frame),entryStatesQ, 10 , 45);
    
    //Symbols
    gtk_fixed_put(GTK_FIXED(frame), labelSymbolsE, 10, 75);
    gtk_fixed_put(GTK_FIXED(frame),entrySymbolsE, 10 , 95);
    
    //Transition Table
    gtk_fixed_put(GTK_FIXED(frame), labelTransitionTableD, 10, 125);
    gtk_fixed_put(GTK_FIXED(frame),entryTransitionTableD, 10 , 145);
    
    //Final
    gtk_fixed_put(GTK_FIXED(frame), labelFinalStatesF, 10, 175);
    gtk_fixed_put(GTK_FIXED(frame),entryFinalStatesF, 10 , 195);
    
    //Run
    gtk_fixed_put(GTK_FIXED(frame), label, 10, 225);
    gtk_fixed_put(GTK_FIXED(frame),entry, 10 , 250);
    gtk_fixed_put(GTK_FIXED(frame), button, 10, 280);
    
    gtk_widget_show_all(window);
    
    //Run
    gtk_main();
    return 0;
}
