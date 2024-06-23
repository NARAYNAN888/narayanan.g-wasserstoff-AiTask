<?php
class My_Chatbot {

    public function run() {
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        add_shortcode('my_chatbot', array($this, 'render_chatbot'));
    }

    public function enqueue_scripts() {
        wp_enqueue_script('chatbot-js', plugin_dir_url(__FILE__) . '../assets/js/chatbot.js', array('jquery'), '1.0', true);
    }

    public function render_chatbot() {
        include plugin_dir_path(__FILE__) . '../templates/chatbot-template.php';
    }
}
