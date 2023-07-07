import asyncio
from datetime import timedelta

from flask import Flask, current_app, jsonify, make_response, request
from temporalio.client import Client

from loyalty_workflow import LoyaltyProgram

app = Flask(__name__)


async def connect_temporal(app):
    client: Client = await Client.connect("localhost:7233")
    app.temporal_client = client


def get_client() -> Client:
    return current_app.temporal_client


@app.route("/<int:user_id>", methods=["POST", "GET"])
async def start(user_id):
    client: Client = get_client()
    if request.method == "POST":
        await client.start_workflow(
            LoyaltyProgram.run,
            id=f"{user_id}",
            task_queue="loyalty-program-task-queue",
            search_attributes={"points": [0]},
        )

        message = jsonify(
            {"message": f"Resource created successfully for user ID: {user_id}"}
        )
        response = make_response(message, 201)
        return response

    elif request.method == "GET":
        handle = client.get_workflow_handle_for(
            LoyaltyProgram.run, workflow_id=f"{user_id}"
        )
        points = await handle.query(LoyaltyProgram.loyalty_details)
        return jsonify({"user_id": user_id, "points": points})

    return jsonify({"message": "This endpoint requires a POST or GET request."})


@app.route("/<int:user_id>/spend_points/<int:points>", methods=["POST"])
async def spend_points(user_id, points):
    client: Client = get_client()
    handle = client.get_workflow_handle_for(
        LoyaltyProgram.run, workflow_id=f"{user_id}"
    )
    if request.method == "POST":
        await handle.signal(LoyaltyProgram.remove_from_points, points)
        message = jsonify({"message": f"{points} spent from user id: {user_id}"})
        response = make_response(message, 200)
        return response

    return jsonify({"message": "This endpoint requires a POST request."})


@app.route("/<int:user_id>/add_points/<int:points>", methods=["POST"])
async def add_points(user_id, points):
    client: Client = get_client()
    handle = client.get_workflow_handle_for(
        LoyaltyProgram.run, workflow_id=f"{user_id}"
    )
    if request.method == "POST":
        await handle.signal(LoyaltyProgram.add_to_points, points)
        message = jsonify({"message": f"{points} added to user id: {user_id}"})
        response = make_response(message, 200)
        return response

    return jsonify({"message": "This endpoint requires a POST request."})


@app.route("/<int:user_id>/exit", methods=["DELETE"])
async def exit(user_id):
    client: Client = get_client()
    handle = client.get_workflow_handle_for(
        LoyaltyProgram.run, workflow_id=f"{user_id}"
    )
    if request.method == "DELETE":
        await handle.signal(LoyaltyProgram.exit)
        message = jsonify({"message": f"User id: {user_id} exited the program."})
        response = make_response(message, 200)
        return response

    return jsonify({"message": "This endpoint requires a DELETE request."})


if __name__ == "__main__":
    asyncio.run(connect_temporal(app))
    app.run(debug=True)
