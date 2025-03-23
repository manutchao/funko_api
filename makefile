start_app:
	docker compose up --build


ping:
	curl -X GET http://localhost:5000/ping