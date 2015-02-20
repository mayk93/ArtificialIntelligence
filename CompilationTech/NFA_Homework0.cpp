#include<gtk/gtk.h>

int main(int argc, char* argv[])
{
    //Initialize Gtk
    gtk_init(&argc,&argv);
    
    //Widgets
    GtkWidget* window;
    GtkWidget* label;
    
    //Widgets Functionality:
    
        //Initialize Widgets
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    label = gtk_label_new("Nondeterministic Finite Automaton");
        //Functionality
    g_signal_connect(window,"delete-event",G_CALLBACK(gtk_main_quit),NULL);
    gtk_window_set_default_size(GTK_WINDOW(window), 500, 500);
    gtk_container_add(GTK_CONTAINER(window),label);
    gtk_widget_show_all(window);
    
    //Run
    gtk_main();
    return 0;
}
