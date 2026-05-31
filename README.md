# Workflow CI - Dhiandika

Repository ini didekasikan untuk memenuhi **Kriteria 3 (Tingkat Advance - 4 pts)** pada Proyek Akhir kelas *Membangun Sistem Machine Learning* Dicoding.

## Profil Siswa
* **Nama**: I Putu Dhiandika Aditya Permana
* **Username Dicoding**: npemburu6

---

## Struktur Folder
```text
Workflow-CI
├── .github/workflows/
│   └── ci.yml                     # GitHub Actions CI Workflow (Build & Push Docker)
└── MLProject/
    ├── MLProject                  # MLflow Project Specification File
    ├── conda.yaml                 # Conda Environment Configuration
    ├── modelling.py               # Retraining script
    ├── namadataset_preprocessing/ # Preprocessed dataset
    │   ├── heart-disease_preprocessed.csv
    │   ├── heart-disease_train.csv
    │   └── heart-disease_test.csv
    └── Tautan ke Docker Hub.txt   # File berisi tautan Docker Hub
```

---

## Deskripsi CI Workflow & Docker
Workflow CI `ci.yml` melakukan tugas berikut secara otomatis:
1. **Triggering**: Berjalan otomatis saat ada perubahan kode di folder `MLProject` atau workflow file.
2. **Retraining**: Menjalankan re-training model menggunakan MLflow Project command `mlflow run`.
3. **Dockerization**: Membangun Docker Image untuk serving model menggunakan perintah `mlflow models build-docker`.
4. **Push to Docker Hub**: Melakukan login otomatis ke Docker Hub menggunakan GitHub Secrets (`DOCKERHUB_USERNAME` & `DOCKERHUB_TOKEN`) dan mengunggah Docker image terbaru dengan tag `latest`.
