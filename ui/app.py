import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import numpy as np
import os

from core.image_loader import ImageLoader
from core.processor import ImageProcessor

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VisionCoreApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Configuration de la fenêtre principale
        self.title("VisionCore - Studio Pro")
        self.geometry("1200x800")
        
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        # Configuration du layout principal (Sidebar fixe, Main extensible)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Variables d'état
        self.original_matrix = None
        self.current_matrix = None

        self._create_sidebar()
        self._create_main_area()

    def _create_sidebar(self):
        """Crée une barre latérale défilante et organisée."""
        # Utilisation d'un cadre défilant pour la sidebar
        self.sidebar_frame = ctk.CTkScrollableFrame(self, width=250, corner_radius=0, label_text="MENU VISIONCORE")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        # --- SECTION : FICHIERS ---
        self.file_section = self._create_section("Gestion de Fichiers")
        ctk.CTkButton(self.file_section, text="Charger Image", command=self.load_image).pack(pady=5, fill="x")
        ctk.CTkButton(self.file_section, text="Sauvegarder", fg_color="#28a745", hover_color="#218838", 
                      command=self.save_image).pack(pady=5, fill="x")
        ctk.CTkButton(self.file_section, text="Réinitialiser", fg_color="transparent", border_width=1, 
                      command=self.reset_image).pack(pady=5, fill="x")

        # --- SECTION : RÉGLAGES DE BASE ---
        self.basic_section = self._create_section("Réglages de Base")
        ctk.CTkButton(self.basic_section, text="Inversion (Négatif)", command=self.apply_inverse).pack(pady=5, fill="x")
        
        self.gamma_label = ctk.CTkLabel(self.basic_section, text="Correction Gamma : 1.0", font=("Arial", 12))
        self.gamma_label.pack(pady=(10, 0))
        self.gamma_slider = ctk.CTkSlider(self.basic_section, from_=0.1, to=3.0, command=self.update_gamma)
        self.gamma_slider.set(1.0)
        self.gamma_slider.pack(pady=5, fill="x")

        # --- SECTION : AMÉLIORATION ---
        self.enhance_section = self._create_section("Amélioration Auto")
        ctk.CTkButton(self.enhance_section, text="Étirement Dyn.", command=self.apply_stretch).pack(pady=5, fill="x")
        ctk.CTkButton(self.enhance_section, text="Égaliser Hist.", command=self.apply_equalization).pack(pady=5, fill="x")

        # --- SECTION : FILTRAGE ---
        self.filter_section = self._create_section("Filtrage Spatial")
        ctk.CTkButton(self.filter_section, text="Flou Gaussien", command=self.apply_blur).pack(pady=5, fill="x")
        ctk.CTkButton(self.filter_section, text="Contours (Sobel)", command=self.apply_sobel).pack(pady=5, fill="x")
        ctk.CTkButton(self.filter_section, text="Filtre Médian", command=self.apply_median).pack(pady=5, fill="x")

        # --- SECTION : SEGMENTATION ---
        self.seg_section = self._create_section("Segmentation & Morpho")
        ctk.CTkButton(self.seg_section, text="Seuillage Otsu", command=self.apply_otsu).pack(pady=5, fill="x")
        ctk.CTkButton(self.seg_section, text="Érosion (Nettoyage)", command=lambda: self.apply_morpho("erosion")).pack(pady=5, fill="x")
        ctk.CTkButton(self.seg_section, text="Dilatation (Expansion)", command=lambda: self.apply_morpho("dilatation")).pack(pady=5, fill="x")

    def _create_section(self, title):
        """Utilitaire pour créer des sections visuelles dans la sidebar."""
        frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        frame.pack(pady=15, padx=5, fill="x")
        label = ctk.CTkLabel(frame, text=title.upper(), font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        label.pack(anchor="w", padx=5, pady=2)
        return frame

    def _create_main_area(self):
        """Zone principale : Image, Histogramme et Statistiques."""
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        self.main_container.grid_rowconfigure(0, weight=4) # Image
        self.main_container.grid_rowconfigure(1, weight=1) # Stats + Hist
        self.main_container.grid_columnconfigure(0, weight=1)

        # 1. Zone Image
        self.image_label = ctk.CTkLabel(self.main_container, text="Aucune image\nChargez un fichier pour commencer", 
                                      fg_color="#151515", corner_radius=10)
        self.image_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # 2. Zone Analyse (Statistiques à gauche, Histogramme à droite)
        self.analysis_frame = ctk.CTkFrame(self.main_container, height=200)
        self.analysis_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.analysis_frame.grid_columnconfigure(1, weight=1) # Hist prend la place
        
        # Sous-zone Statistiques
        self.stats_label = ctk.CTkLabel(self.analysis_frame, text="Stats : --", justify="left", anchor="nw",
                                      font=("Consolas", 12), padx=15, pady=15)
        self.stats_label.grid(row=0, column=0, sticky="nsew")

        # Sous-zone Histogramme
        self.fig = Figure(figsize=(4, 1.5), dpi=80, facecolor='#2b2b2b')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#2b2b2b')
        self.ax.tick_params(colors='white', labelsize=7)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.analysis_frame)
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

    # --- LOGIQUE DE TRAITEMENT ---

    def display_image(self, matrix: np.ndarray):
        """Affiche la matrice et met à jour les analyses."""
        image_pil = Image.fromarray(matrix)
        
        # Redimensionnement dynamique
        w, h = self.image_label.winfo_width(), self.image_label.winfo_height()
        if w < 100: w, h = 800, 500 # Valeurs par défaut au démarrage
        
        image_pil.thumbnail((w, h), Image.Resampling.LANCZOS)
        tk_image = ctk.CTkImage(light_image=image_pil, dark_image=image_pil, size=image_pil.size)
        
        self.image_label.configure(image=tk_image, text="")
        self.update_analysis()

    def update_analysis(self):
        """Met à jour l'histogramme et les chiffres clés."""
        if self.current_matrix is not None:
            # 1. Histogramme
            hist = ImageProcessor.get_histogram(self.current_matrix)
            self.ax.clear()
            self.ax.bar(range(256), hist, width=1.0, color='#1f538d')
            self.ax.set_xlim([0, 255])
            self.ax.get_yaxis().set_visible(False)
            self.canvas.draw()

            # 2. Statistiques
            stats = ImageProcessor.get_stats(self.current_matrix)
            txt = (f"DIMENSIONS : {stats['dimensions'][1]}x{stats['dimensions'][0]}\n"
                   f"LUMINANCE  : {stats['moyenne_luminance']:.2f}\n"
                   f"CONTRASTE  : {stats['std_dev']:.2f}\n"
                   f"MIN / MAX  : {stats['min_val']} / {stats['max_val']}")
            self.stats_label.configure(text=txt)

    # --- CALLBACKS DES BOUTONS ---

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.jpeg;*.png;*.bmp;*.pgm")])
        if file_path:
            self.current_matrix = ImageLoader.load(file_path)
            self.original_matrix = self.current_matrix.copy()
            self.gamma_slider.set(1.0)
            self.display_image(self.current_matrix)

    def save_image(self):
        if self.current_matrix is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path: ImageLoader.save(self.current_matrix, file_path)

    def apply_inverse(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.inverse(self.current_matrix)
            self.display_image(self.current_matrix)

    def update_gamma(self, value):
        self.gamma_label.configure(text=f"Correction Gamma : {value:.1f}")
        if self.original_matrix is not None:
            self.current_matrix = ImageProcessor.apply_gamma(self.original_matrix, value)
            self.display_image(self.current_matrix)

    def apply_stretch(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.stretch_contrast(self.current_matrix)
            self.display_image(self.current_matrix)

    def apply_equalization(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.equalize_histogram(self.current_matrix)
            self.display_image(self.current_matrix)

    def apply_blur(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.blur_gaussian(self.current_matrix)
            self.display_image(self.current_matrix)

    def apply_sobel(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.detect_edges_sobel(self.current_matrix)
            self.display_image(self.current_matrix)

    def reset_image(self):
        if self.original_matrix is not None:
            self.current_matrix = self.original_matrix.copy()
            self.gamma_slider.set(1.0)
            self.display_image(self.current_matrix)

    def apply_median(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.filter_median(self.current_matrix)
            self.display_image(self.current_matrix)

    def apply_otsu(self):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.threshold_otsu(self.current_matrix)
            self.display_image(self.current_matrix)

    def apply_morpho(self, mode):
        if self.current_matrix is not None:
            self.current_matrix = ImageProcessor.morpho_operation(self.current_matrix, mode)
            self.display_image(self.current_matrix)