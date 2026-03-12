# Attendance_management_system
This is a smart attendance management system 

Project Name: Smart Attendance System (with Admin Features)

## Features:

1. Admin Login
Admin একটি নিরাপদ লগইন ব্যবহার করে সিস্টেমে প্রবেশ করবে। লগইন করার পর Admin সমস্ত সেটআপ এবং management কাজ করতে পারবে।

### 2. Teacher Management
- Admin নতুন Teachers add করতে পারবে।  
- Teachers-এর জন্য username, password, email এবং mobile number নির্ধারণ করা হবে।  
- Admin Teachers edit বা delete করতে পারবে।  
- Teachers-এর username বা password পরিবর্তন করা যাবে যখন প্রয়োজন।

### 3. Semester and Subject Assignment
- Admin প্রতিটি Teacher-কে নির্দিষ্ট semester এবং subject assign করতে পারবে।  
- একাধিক subject একবারে assign করা যাবে।  
- Teacher login করার পরে শুধু তার assigned subjects এবং semester দেখাবে, তাই ভুল selection কম হবে।

### 4. Admin Dashboard
- Admin Dashboard-এ সমস্ত Teachers-এর record সংরক্ষিত থাকবে।  
- কোন Teacher কোন subject এবং semester handle করছে তা সহজেই দেখা যাবে।  

### 5. Teacher Login
- Teacher তার username এবং password ব্যবহার করে লগইন করবে।  
- লগইন করার পর Teacher একটি personal dashboard পাবে, যেখানে তার assigned semester এবং subjects দেখা যাবে।

### 6. Teacher Attendance Dashboard
- Teacher তার assigned semester select করবে।  
- সেই semester অনুযায়ী system তার assigned subjects দেখাবে।  
- Teacher date select করে students-এর উপস্থিতি (Present / Absent) mark করবে।  
- একবার Student list add করলে ওই semester এবং subject-এর জন্য পুনরায় add করতে হবে না।  
- Students add করার সময় Teacher student-এর roll number এবং name store করবে।  
- পুরো semester-এর জন্য attendance শুধু Present / Absent button click করেই করা যাবে।

### 7. Semester End Control
- Semester শেষ করা শুধু Admin করতে পারবে।  
- ভুলে semester end করলে undo/redo option থাকবে।  
- Semester end করার পর ঐ semester-এর সমস্ত attendance history save থাকবে।

### 8. Student Attendance Tracking
- Students roll number ব্যবহার করে search করলে personal dashboard দেখাবে।  
- Dashboard-এ দেখা যাবে কতদিন উপস্থিত ছিল, কতদিন অনুপস্থিত ছিল, এবং overall summary।

### 9. Multiple Subject Assignment
- Admin একাধিক subject একবারে নির্দিষ্ট Teacher এবং semester-এ assign করতে পারবে।  
- Teachers-এর কাজ সহজ হবে এবং system structured থাকবে।

## Folder structure
```
Attendance_management_system/
│
├── run.py                  # Main Flask app runner
├── requirements.txt        # Project dependencies
├── README.md               # Project overview & instructions
├── config.py               # Configuration (DB URI, secret key, etc.)
│
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── models.py           # SQLAlchemy ORM models (Teacher, Student, Subject, Attendance)
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── teachers/
│   │   │   │   ├── dashboard.css        # Teacher dashboard styles
│   │   │   │   ├── attendance.css       # Teacher attendance page styles
│   │   │   │   └── login.css            # Teacher login page styles
│   │   │   │
│   │   │   ├── admin/
│   │   │   │   ├── dashboard.css        # Admin dashboard main styles
│   │   │   │   ├── manage_teachers.css # Admin manage teachers page
│   │   │   │   └── login.css            # Admin login page
│   │   │   │
│   │   │   └── students/
│   │   │       ├── dashboard.css        # Student dashboard
│   │   │       └── attendance.css       # Student attendance view
│   │   │
│   │   └── js/
│   │       ├── teachers/
│   │       │   ├── dashboard.js         # Teacher dashboard interactivity
│   │       │   ├── attendance.js        # Attendance mark toggle / AJAX
│   │       │   └── validation.js        # Form validation
│   │       │
│   │       ├── admin/
│   │       │   ├── dashboard.js         # Admin dashboard interactivity
│   │       │   ├── manage_teachers.js  # Add/Edit/Delete teacher AJAX
│   │       │   └── undo_redo.js         # Semester end undo/redo
│   │       │
│   │       └── students/
│   │           ├── dashboard.js         # Attendance summary charts / search
│   │           └── filter.js            # Roll number search, table filter
│   │
│   ├── templates/
│   │   ├── admin/
│   │   │   ├── login.html                # Admin login page
│   │   │   ├── dashboard.html            # Main dashboard
│   │   │   ├── manage_teachers.html      # Add/Edit/Delete teachers
│   │   │   ├── semester_end.html         # Semester end / undo redo
│   │   │   └── change_password.html      # Admin change username/password
│   │   │
│   │   ├── teachers/
│   │   │   ├── login.html                # Teacher login
│   │   │   ├── dashboard.html            # Dashboard overview
│   │   │   ├── attendance.html           # Attendance mark page
│   │   │   └── subject_select.html       # Subject/Semester selection page
│   │   │
│   │   └── students/
│   │       ├── dashboard.html            # Student view of attendance
│   │       └── search.html               # Roll number search page
│   │
│   └── routes/
│       ├── admin/
│       │   ├── __init__.py               # Admin blueprint init
│       │   ├── login_routes.py           # Admin login handling
│       │   ├── dashboard_routes.py       # Admin dashboard routes
│       │   ├── manage_teachers_routes.py # Add/Edit/Delete teachers
│       │   └── semester_routes.py        # Semester end / undo redo routes
│       │
│       ├── teachers/
│       │   ├── __init__.py
│       │   ├── login_routes.py
│       │   ├── dashboard_routes.py
│       │   └── attendance_routes.py
│       │
│       └── students/
│           ├── __init__.py
│           ├── dashboard_routes.py
│           └── search_routes.py
```
