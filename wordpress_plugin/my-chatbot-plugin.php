<?php
/**
 * Plugin Name: My Chatbot Plugin
 * Description: A plugin to integrate the RAG-based Chatbot with CoT for WordPress.
 * Version: 1.0
 * Author: Your Name
 */

require_once plugin_dir_path(__FILE__) . 'includes/class-my-chatbot.php';

function initialize_my_chatbot() {
    $plugin = new My_Chatbot();
    $plugin->run();
}
add_action('plugins_loaded', 'initialize_my_chatbot');
?>