#include<gtk/gtk.h>

int main(int argc, char* argv[])
{
    //Initialize Gtk
    gtk_init(&argc,&argv);
    
    //Widgets
    GtkWidget* window;
    
    //Widgets Functionality
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    g_signal_connect(window,"delete-event",G_CALLBACK(gtk_main_quit),NULL);
    gtk_window_set_default_size(GTK_WINDOW(window), 500, 500);
    gtk_widget_show(window);
    
    //Run
    gtk_main();
    return 0;
}
