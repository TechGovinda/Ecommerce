# 🛒 E-Commerce Website  

An E-commerce web application built by following the **Bfive Tech YouTube tutorial series**, using **Django (backend)** and **Tailwind CSS with Flowbite (frontend)**.  

---

## 🚀 Features
- User authentication (Login / Register / Logout)
- Product listing and details page
- Add to cart functionality
- Checkout process
- Order management
- Responsive UI with Tailwind CSS & Flowbite

---

## 🛠️ Tech Stack
- **Backend:** Django, Django ORM, SQLite/PostgreSQL  
- **Frontend:** Tailwind CSS, Flowbite (Tailwind Components)  
- **Other Tools:** Vite (optional for Tailwind build), Git, GitHub  

---

## 📂 Project Structure
```
ecommerce/
│── core/              # Main project settings
│── store/             # Product & cart logic
│── accounts/          # User authentication
│── templates/         # HTML templates
│── static/            # CSS, JS, Images
│── manage.py
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce.git
   cd ecommerce
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open in browser → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🎨 Tailwind & Flowbite Setup

If Tailwind is not already built, run:
```bash
npm install
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Flowbite is included for pre-built UI components. Check docs: [Flowbite](https://flowbite.com/)

---

## 📸 Screenshots
(Add your project screenshots here)

---

## 📺 Reference
This project is built by following the tutorial series on **Bfive Tech YouTube Channel**.  
👉 [Bfive Tech YouTube](https://www.youtube.com/@BfiveTech)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is for learning purposes. Free to use and modify.
