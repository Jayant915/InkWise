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

  <img width="355" height="300" alt="image" src="https://github.com/user-attachments/assets/54dffb59-36df-4d59-8626-45d5090dda73" />


---

## 📂 Project Structure

InkWise/<br>
│── media/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Uploaded images<br>
│── myapp/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;#Core application logic<br>
│── mysite/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Django project configuration<br>
│── db.sqlite3  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#SQLite database (default)<br>
│── manage.py &nbsp;&nbsp;&nbsp;&nbsp;#Django project manager<br>

---

## ⚙️ Installation & Setup


**1. Clone the repository:**
```
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

## 📈 Performance Summary

<img width="493" height="437" alt="image" src="https://github.com/user-attachments/assets/bf2b5a09-2b79-4e12-ae90-8705848f04c6" /> <img width="495" height="432" alt="image" src="https://github.com/user-attachments/assets/933a952e-e3f8-4d6a-84ed-da43f340dfd5" />




---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

## 👨‍💻 Author

Developed by **Jayant915**<br>
InkWise – Making handwritten notes smarter ✨

