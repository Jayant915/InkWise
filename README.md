# 🖋️ InkWise

InkWise is a **smart handwriting recognition system** that extracts and digitizes handwritten text into editable, searchable formats.  
It leverages **OCR (Optical Character Recognition)** technology and provides a simple web interface built using **Django**.

---

## 🚀 Features
- Upload handwritten notes or images.
- Extract text using OCR.
- View and copy recognized text.
- Clean, simple Django-based web app.
- Stores uploaded images and results for later use.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Database:** MySQL
- **OCR API:** OCR.Space, pytesserect
- **Frontend:** HTML, CSS, Bootstrap

---

```

## 📂 Project Structure

InkWise/
│── media/    Uploaded images
│── myapp/    Core application logic
│── mysite/   Django project configuration
│── db.sqlite3  SQLite database (default)
│── manage.py  Django project manager

```

---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/InkWise.git
   cd InkWise
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open in browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📸 Usage

1. Upload an image containing handwritten text.
2. The system will process it using OCR.
3. Extracted text will be displayed on the results page.
4. Copy or save the digitized text.

---

## 🔮 Future Enhancements

* Support for multiple OCR engines (Google Vision, EasyOCR).
* Text-to-Speech integration for extracted content.
* Multi-language handwriting recognition.
* User authentication & saved notes history.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

## 👨‍💻 Author

Developed by **Jayant915**
InkWise – Making handwritten notes smarter ✨

