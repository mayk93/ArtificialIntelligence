#include <gtk/gtk.h>

static void onClick(GtkWidget *widget, gpointer data)
{
    g_print("%s\n",gtk_entry_get_text(GTK_ENTRY(data)));
}

int main(int argc, char*argv[])
{
    gtk_init(&argc,&argv);
    GtkWidget *window, *table, *label, *button , *entry, *hbox;
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    g_signal_connect(window,"delete_event",G_CALLBACK(gtk_main_quit),NULL);
    
    table  = gtk_table_new(3,2,0); //2 Rows, 2 Columns, Non-Homogenous
    
    button = gtk_button_new_with_mnemonic("_Work");
    label  = gtk_label_new("My label");
    gtk_table_attach(GTK_TABLE(table),label,0,1,0,1,GTK_FILL,GTK_FILL,0,0);
    gtk_table_attach(GTK_TABLE(table),button,1,2,0,1,GTK_FILL,GTK_FILL,0,0);
    
    button = gtk_button_new_with_mnemonic("W_ork");
    label  = gtk_label_new("My other label");
    gtk_table_attach(GTK_TABLE(table),label,0,1,1,2,GTK_FILL,GTK_FILL,0,0);
    gtk_table_attach(GTK_TABLE(table),button,1,2,1,2,GTK_FILL,GTK_FILL,0,0);
    
    entry = gtk_entry_new();
    button = gtk_button_new_with_mnemonic("_Text");
    g_signal_connect(button,"clicked",G_CALLBACK(onClick),entry);
    gtk_table_attach(GTK_TABLE(table),entry,0,1,2,3,GTK_FILL,GTK_FILL,0,0);
    gtk_table_attach(GTK_TABLE(table),button,1,2,2,3,GTK_FILL,GTK_FILL,0,0);
    
    /*
    label  = gtk_label_new("My third label");
    hbox = gtk_hbox_new(50,50);
    gtk_box_pack_start(GTK_BOX(hbox),entry,0,0,0);
    gtk_box_pack_start(GTK_BOX(hbox),button,0,0,0);
    gtk_container_add(GTK_CONTAINER(window),hbox);
    */
    
    gtk_container_add(GTK_CONTAINER(window),table);
    gtk_window_set_default_size(GTK_WINDOW(window), 250, 250);
    
    gtk_widget_show_all(window);
    gtk_main();
    return 0;
}
