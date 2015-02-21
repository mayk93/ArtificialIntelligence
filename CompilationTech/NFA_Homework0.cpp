#include<gtk/gtk.h>
#include<iostream>
#include <stdlib.h>

using namespace std;

gint numberOfClicks = 0;

static void onClick(GtkWidget **entry, GtkWidget *widget)
{
    /*
    g_print("%s\n",gtk_entry_get_text(GTK_ENTRY(data)));
    cout<<"Here 0\n";
    long int numberOfStates = -1;
    cout<<"Here 1\n";
    char* pEnd;
    cout<<"Here 2\n";
    numberOfStates = strtol (gtk_entry_get_text(GTK_ENTRY(data)), &pEnd, 10);
    cout<<"Here 3\n";
    g_print("%ld\n",numberOfStates);
    cout<<"Here 4\n";
    */
    
  GtkWidget *entry_ptr_a = entry[0];
  GtkWidget *entry_ptr_s = entry[1];
  GtkWidget *entry_ptr_t = entry[2];
  GtkWidget *entry_ptr_v = entry[3];
  GtkWidget *entry_ptr_r = entry[4];

  const gchar *a, *s, *t, *v, *r;


  a = gtk_entry_get_text(GTK_ENTRY (entry_ptr_a));
  s = gtk_entry_get_text(GTK_ENTRY (entry_ptr_s));
  t = gtk_entry_get_text(GTK_ENTRY (entry_ptr_t));
  v = gtk_entry_get_text(GTK_ENTRY (entry_ptr_v));
  r = gtk_entry_get_text(GTK_ENTRY (entry_ptr_r));


  printf ("Result: %s , %s, %s, %s, %s\n", a, s, t, v, r);  
}

int main(int argc, char* argv[])
{
    //Variables
    const char* titleText      = "Nondeterministic Finite Automaton";
    const char* statesText     = "Enter number of states";
    const char* symbolsText    = "Enter Symbols";
    const char* transitionText = "Enter path to transition table";
    const char* finalText      = "Enter final states";
    
    //Initialize Gtk
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
