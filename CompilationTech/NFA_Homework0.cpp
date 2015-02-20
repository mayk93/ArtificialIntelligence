#include<gtk/gtk.h>

int main(int argc, char* argv[])
{
    //Variables
    const char* titleText = "Nondeterministic Finite Automaton";
    const char* buttonText = "Test Word";
    
    //Initialize Gtk
    gtk_init(&argc,&argv);
    
    //Widgets
    GtkWidget* window;
    GtkWidget* label;
    GtkWidget* buttonLabel;
    GtkWidget* entry;
    GtkWidget* button;
    
    //Widgets Functionality:
        //Initialize Widgets
    window   = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    label    = gtk_label_new("");
    buttonLabel    = gtk_label_new("");
    entry    = gtk_entry_new();
    button  = gtk_button_new(); //Button is A container. Add label to it.
        //Functionality
    gtk_label_set_text(GTK_LABEL(label),titleText);
    gtk_label_set_text(GTK_LABEL(buttonLabel),buttonText);
    g_signal_connect(window,"delete-event",G_CALLBACK(gtk_main_quit),NULL);
    gtk_window_set_default_size(GTK_WINDOW(window), 500, 500);
    //gtk_container_add(GTK_CONTAINER(window),label);
    //gtk_container_add(GTK_CONTAINER(window),entry);
    gtk_container_add(GTK_CONTAINER(window),button);
    gtk_widget_show_all(window);
    
    //Run
    gtk_main();
    return 0;
}
