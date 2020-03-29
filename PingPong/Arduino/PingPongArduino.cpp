#include <Arduino.h>

static const int ledPin=13;
void setup() {
	pinMode(ledPin, OUTPUT);
	Serial.begin(115200);
}

void loop() {
	if (Serial.available()) {
		digitalWrite(ledPin, HIGH);
		const char incoming=Serial.read();
		if (!isPrintable(incoming)) {
			// Receiving something like '\0', '\1', ...
			// Probably, in hand shake doing ping pong
			// We just do an echo
			Serial.write(incoming);
		} else {
			// Here we go: at last some meaningful data
			String message = "Got Command:<";
			message.concat(incoming);
			message.concat(">");
			for (int i=0; i<message.length(); i++) {
				Serial.write(message.charAt(i));
			}
			// Finish message with a '\0'
			// So the client knows we're done
			// with the reply
			Serial.write('\0');
		}
		digitalWrite(ledPin, LOW);
	}
}
