#include <mqtt/async_client.h>

//const std::string SERVER_ADDRESS("3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud:8883");
const std::string SERVER_ADDRESS("tcp://20.79.70.109:8883");
const std::string CLIENT_ID("");
const std::string TOPIC("sensehat");
const std::string USERNAME("mvp2023");
const std::string PASSWORD("wzq6h2hm%WLaMh$KYXj5");

int main()
{
    //mqtt::log::set_level(mqtt::log::DEBUG);

    mqtt::async_client client(SERVER_ADDRESS, CLIENT_ID);

    mqtt::connect_options connOpts;
    connOpts.set_keep_alive_interval(20);
    connOpts.set_clean_session(true);

    // Set username and password
    connOpts.set_user_name("mvp2023");
    connOpts.set_password("wzq6h2hm%WLaMh$KYXj5");

    try {
        mqtt::token_ptr conntok = client.connect(connOpts);
        conntok->wait();

        mqtt::message_ptr pubmsg = mqtt::make_message(TOPIC, "Hello, world!");
        pubmsg->set_qos(1);
        client.publish(pubmsg)->wait_for(std::chrono::seconds(10));

        // Disconnect
        conntok = client.disconnect();
        conntok->wait();
    }
    catch (const mqtt::exception& exc) {
        std::cerr << "Error: " << exc.what() << std::endl;
        return 1;
    }

    return 0;
}
