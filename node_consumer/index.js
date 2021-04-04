const Kafka = require("no-kafka");

const CONSUMER = new Kafka.SimpleConsumer(
	{
		"connectionString": "127.0.0.1:9092"
	}
);

let handler = (messageSet, topic, partition) => {
	messageSet.forEach((m) => {
		let read_value = m.message.value.toString('utf8');
		console.log(`TOPIC - ${topic} - MESSAGE - ${read_value}`);
	});
};

CONSUMER.init().then(() => {
	return CONSUMER.subscribe("foo-topic", 0, {offset: 20, maxBytes: 3000}, handler);
});
