#include<gtk/gtk.h>
#include<iostream>

using namespace std;

gint numberOfClicks = 0;

static void onClick(GtkWidget* widget,gpointer data)
{
    g_print("Button Pressed.\n");
    cout<<"Old: "<<numberOfClicks<<endl;
    numberOfClicks = numberOfClicks + 1;
    cout<<"New: "<<numberOfClicks<<endl<<endl;
}

int main(int argc, char* argv[])
{
    //Variables
    const char* titleText = "Nondeterministic Finite Automaton";
    
    //Initialize Gtk
    gtk_init(&argc,&argv);
    
    //Widgets
    GtkWidget* window;
    GtkWidget* label;
    GtkWidget* entry;
    GtkWidget* button;
    GtkWidget* frame;
    
    //Widgets Functionality:
        //Initialize Widgets
    window   = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    label    = gtk_label_new("");
    entry    = gtk_entry_new();
    button   = gtk_button_new_with_label("Test Word");
    frame    = gtk_fixed_new();
        //Functionality
    gtk_label_set_text(GTK_LABEL(label),titleText);
    g_signal_connect(window,"delete-event",G_CALLBACK(gtk_main_quit),NULL);
    g_signal_connect(button,"clicked",G_CALLBACK(onClick),NULL);
    gtk_window_set_title(GTK_WINDOW(window),titleText);
    gtk_window_set_default_size(GTK_WINDOW(window), 500, 500);
    gtk_widget_set_size_request(button, 100, 25);
    gtk_container_add(GTK_CONTAINER(window), frame);
    gtk_fixed_put(GTK_FIXED(frame), label, 10, 25);
    gtk_fixed_put(GTK_FIXED(frame),entry, 10 , 50);
    gtk_fixed_put(GTK_FIXED(frame), button, 10, 80);
    gtk_widget_show_all(window);
    
    //Run
    gtk_main();
    return 0;
}
