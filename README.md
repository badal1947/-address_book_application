step 1=> open cmd
step 2=> git --version
step 3=> git clone https://github.com/badal1947/-address_book_application.git
step 4=> Enter the project folder
        cd "\-address_book_application\Eastvantage_2"

step 5=> python -m venv .venv
step 6=> .venv\Scripts\activate
step 7=> pip install -r requirements.txt
step 8=> uvicorn main:app --reload --host 127.0.0.1 --port 8000
step 9=> http://127.0.0.1:8000/docs
