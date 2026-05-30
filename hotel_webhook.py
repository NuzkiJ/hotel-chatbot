from flask import Flask, request, jsonify
import sqlite3
import random

app = Flask(__name__)

# Generate unique booking ID

def generate_booking_id():
    return f"BER{random.randint(0,99999):05d}"

@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json()
    intent = req["queryResult"]["intent"]["displayName"]

# TRACK BOOKING

    if intent == "BookingID (2.2.1)":

        booking_id = req["queryResult"]["parameters"].get("booking_id")

        conn = sqlite3.connect("hotel_bookings.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bookings WHERE booking_id=?", (booking_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            message = f"""Thank you. Here are your booking details.

            Name: {row[1]}
            Guests: {int(row[2])}
            Room Type: {row[3]}
            Check-in: {row[4]}
            Check-out: {row[5]}
            Breakfast: {row[6]}
            Email: {row[7]}
            Payment Method: {row[8]}

            Your reservation is confirmed."""
        else:
            message = "Sorry, we could not find a booking with that ID."

        return jsonify({"fulfillmentText": message})

# GET DATA FROM CONTEXT

    contexts = req["queryResult"].get("outputContexts", [])
    booking_params = {}

    for context in contexts:
        if "booking_data" in context["name"]:
            booking_params = context.get("parameters", {})

    name = booking_params.get("name")
    guests = booking_params.get("guests")
    room_type = booking_params.get("room_type")
    checkin_date = booking_params.get("checkin_date")
    checkout_date = booking_params.get("checkout_date")
    breakfast_option = booking_params.get("breakfast_option")
    email = booking_params.get("Email")
    payment_method = booking_params.get("payment_method")

    if isinstance(name, dict):
        name = name.get("name")

    # Clean data
    name = name.title() if name else ""
    room_type = room_type.title() if room_type else ""
    payment_method = payment_method.title() if payment_method else ""
    breakfast_option = breakfast_option.title() if breakfast_option else "No"

    guests = int(guests) if guests else 0
    checkin_date = checkin_date.split("T")[0] if checkin_date else ""
    checkout_date = checkout_date.split("T")[0] if checkout_date else ""


# CONFIRM BOOKING (ONLY YES)

    if intent == "Confirm (2.1.9)":

        booking_id = generate_booking_id()

        conn = sqlite3.connect("hotel_bookings.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (booking_id, name, guests, room_type, checkin_date, checkout_date, breakfast_option, email, payment_method))

        conn.commit()
        conn.close()

        message = f"""Your reservation has been successfully booked!

                    Booking ID: {booking_id}

                    A confirmation email with your Booking ID will be sent shortly.

                    Thank you for choosing Grand Ceylonara Berlin!"""

        return jsonify({"fulfillmentText": message})


# DEFAULT → SHOW CONFIRMATION

    message = f"""Please confirm your reservation:

                Name: {name}
                Guests: {guests}
                Room Type: {room_type}
                Check-in: {checkin_date}
                Check-out: {checkout_date}
                Breakfast: {breakfast_option}
                Email: {email}
                Payment Method: {payment_method}

                Do you confirm the booking?"""

    return jsonify({"fulfillmentText": message})


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)