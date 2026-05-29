import os
import shutil

# Target directory
base_dir = "named"

# Directory names
dirs = {
    "01_His_Image_Ministries": "01_His_Image_Ministries",
    "02_Makerere_AI_Lab_M_vet": "02_Makerere_AI_Lab_M_vet",
    "03_Ekijul_Real_Estate": "03_Ekijul_Real_Estate",
    "04_Kazo_Technical_School": "04_Kazo_Technical_School",
    "05_Tukue_Pamoja": "05_Tukue_Pamoja",
    "06_Morgan_Concrete_Services": "06_Morgan_Concrete_Services",
    "07_Sawers_Harvest_Cafe": "07_Sawers_Harvest_Cafe",
    "08_Inspire_Coffee": "08_Inspire_Coffee",
    "09_Zion_Shelter": "09_Zion_Shelter",
    "10_Antioch_Resource_Center": "10_Antioch_Resource_Center",
    "11_Willowhill_Golden_Doodles": "11_Willowhill_Golden_Doodles",
    "12_Mbarara_Junior_School": "12_Mbarara_Junior_School",
    "13_Medium_Blog_Articles": "13_Medium_Blog_Articles",
    "14_Miscellaneous": "14_Miscellaneous"
}

# Core file mapping
mapping = {
    # His Image Ministries (HIM)
    "HIM love them both campaign banner.png": "01_His_Image_Ministries",
    "HIM outdoor sign: poster for let's talk about life.png": "01_His_Image_Ministries",
    "Him & mercy for mamas katanga out reach flyer (social media).png": "01_His_Image_Ministries",
    "Him Apprel design (Reflector jacket).png": "01_His_Image_Ministries",
    "Him Silicon Wristbands.png": "01_His_Image_Ministries",
    "Him Social media flyer (celebrating motherhood).png": "01_His_Image_Ministries",
    "Him love them both Shirt design for campaign.png": "01_His_Image_Ministries",
    "Him social media flyer on Singlehood & marriage.png": "01_His_Image_Ministries",
    "His I mage Ministries Flyer.png": "01_His_Image_Ministries",
    "His Image Ministries  Trifold Broncure design.png": "01_His_Image_Ministries",
    "His image minstries (HIM) pen design impression.png": "01_His_Image_Ministries",
    "His image minstries MAP rollup banner design.png": "01_His_Image_Ministries",
    "His image minstries Social media Flyer MAP Program.png": "01_His_Image_Ministries",
    "His image minstries Tear drop banner.png": "01_His_Image_Ministries",

    # Makerere AI Lab & M-vet
    "M-VET Stickers.png": "02_Makerere_AI_Lab_M_vet",
    "M-VET UI design (Transforming the Agriculture world inforgraphics).png": "02_Makerere_AI_Lab_M_vet",
    "M-VET calendar.png": "02_Makerere_AI_Lab_M_vet",
    "M-VET certificate Design.png": "02_Makerere_AI_Lab_M_vet",
    "M-vet Hackathon Makerere.png": "02_Makerere_AI_Lab_M_vet",
    "M-vet Social media post (Datasets for Machine learning Diagnostics in Livestock).png": "02_Makerere_AI_Lab_M_vet",
    "M-vet machine learning for Livestock Hackton Rollup banner.png": "02_Makerere_AI_Lab_M_vet",
    "Machine learning for livestock Hackaton dummy awards (M-VET).png": "02_Makerere_AI_Lab_M_vet",
    "Makerere AI Lab & CV4A Cap design.png": "02_Makerere_AI_Lab_M_vet",
    "Makerere AI Lab Building machine transtion models for informal speech poster.png": "02_Makerere_AI_Lab_M_vet",
    "Makerere AI Lab Building machine transition models for informal speech poster.png": "02_Makerere_AI_Lab_M_vet",
    "Makerere AI lab Automatic speech Recorgnition..png": "02_Makerere_AI_Lab_M_vet",
    "Makerere Ai lab posters Mining Radiocasts for Community percetion on COVID19 Using Automated Speech.png": "02_Makerere_AI_Lab_M_vet",
    "Makerere M-VET Leveraging data poster.png": "02_Makerere_AI_Lab_M_vet",
    "makerere Ai lab posters (Cassava).png": "02_Makerere_AI_Lab_M_vet",
    "Mvet.png": "02_Makerere_AI_Lab_M_vet",

    # Ekijul Real Estate
    "Ekijul Real estate & developeers logo.png": "03_Ekijul_Real_Estate",
    "Ekijul brand Identity (key holder).png": "03_Ekijul_Real_Estate",
    "Ekijul brand identity cap design.png": "03_Ekijul_Real_Estate",
    "Ekijul construction helment : brand identity.png": "03_Ekijul_Real_Estate",
    "Ekijul real esate & developers brand identity.png": "03_Ekijul_Real_Estate",
    "Ekijul real estate cape mockup :brand identity.png": "03_Ekijul_Real_Estate",

    # Kazo Technical School
    "KAZO TECH SCH TEAR DROPS minmal white print 2.pdf": "04_Kazo_Technical_School",
    "Kazo Technical School Award Plaque.jpg": "04_Kazo_Technical_School",
    "Kazo Technical Shool Teardrop banner design.png": "04_Kazo_Technical_School",
    "Kazo technical School rollup banner design.png": "04_Kazo_Technical_School",
    "Kazo technical School sticker design.png": "04_Kazo_Technical_School",
    "Kazo technical school Apprel design (reflector jact).png": "04_Kazo_Technical_School",
    "Kazo technical school registration in progress for new class.png": "04_Kazo_Technical_School",
    "Kazo technicale school social media flyer.png": "04_Kazo_Technical_School",

    # Tukue Pamoja
    "Tukue Pamoja barand identity Sweater Shirt.png": "05_Tukue_Pamoja",
    "Tukue Pamoja bussiness cards. brand identity.png": "05_Tukue_Pamoja",
    "Tukue pamoja logo on trifold broncure mockup.png": "05_Tukue_Pamoja",
    "Tukue pamoja logo.png": "05_Tukue_Pamoja",

    # Morgan Concrete Services
    "Morgan Concrete Services brand identity.jpg": "06_Morgan_Concrete_Services",
    "Morgan Concrete services apprel design Hoodie.jpg": "06_Morgan_Concrete_Services",
    "Morgan concrete services aprel design.jpg": "06_Morgan_Concrete_Services",
    "morgan concrete Services logo design.jpg": "06_Morgan_Concrete_Services",

    # Sawers Harvest Cafe
    "Sawers harvest  cafe brand identity (coffee cup) .jpg": "07_Sawers_Harvest_Cafe",
    "Sawers harvest brand identity design.jpg": "07_Sawers_Harvest_Cafe",
    "sawers harvest cafe brand identity Water bottle.jpg": "07_Sawers_Harvest_Cafe",
    "sawers havest Cafe logo design.jpg": "07_Sawers_Harvest_Cafe",

    # Inspire Coffee
    "Insipire digtal coffee fund ui .png": "08_Inspire_Coffee",
    "Inspire Digtal coffee fund UI design.png": "08_Inspire_Coffee",
    "Inspire coffee Fund Rollup banner.png": "08_Inspire_Coffee",

    # Zion Shelter
    "Zion Shelter X-mass charity Flyer.png": "09_Zion_Shelter",
    "Zion Shelter brand Identy (Laptop Stickers).png": "09_Zion_Shelter",
    "Zion Shelter brand identity: Application.png": "09_Zion_Shelter",

    # Antioch Resource Center
    "Antioch Christian Resource Center Services flyer.png": "10_Antioch_Resource_Center",
    "Antioch Christian Resource Center inductive bible outdoor poster..png": "10_Antioch_Resource_Center",

    # Willowhill Golden Doodles
    "Willowhill golden doodles brand ideintity.jpg": "11_Willowhill_Golden_Doodles",
    "Willowhill golden doodles brand identity design.jpg": "11_Willowhill_Golden_Doodles",

    # Mbarara Junior School
    "Mbarara Junior School exercise book cover design.png": "12_Mbarara_Junior_School",
    "Mbarara junior execise book design opt2.png": "12_Mbarara_Junior_School",

    # Medium Blog Articles
    "Blog post by Samson Iron (Navigating the Chaos).png": "13_Medium_Blog_Articles",
    "Blog post written by Samson Iron (How Animals could inspire the smart phones of the future).png": "13_Medium_Blog_Articles",
    "Blog post written by Samson Iron (The Cats Eyes and Road Safety).png": "13_Medium_Blog_Articles",
    "Blog post written by Samson Iron (The waggle dance).png": "13_Medium_Blog_Articles",
    "Blog posts published on Empowering First responders in uganda Written by samson Iron.png": "13_Medium_Blog_Articles",
    "Navigating the Chaos. Ablog post Writen by Samson and published on Medium.png": "13_Medium_Blog_Articles",

    # Miscellaneous/Other specific projects
    "A rise Uganda (Celebrating Ugana's Indpendence).png": "14_Miscellaneous",
    "Ami all purpose floor packaging design.png": "14_Miscellaneous",
    "BH motion brand identity.png": "14_Miscellaneous",
    "Brooks Landscape Brand identity design.png": "14_Miscellaneous",
    "FAbre African  music logo design .png": "14_Miscellaneous",
    "FRC brand design.png": "14_Miscellaneous",
    "Government of Netherlands & European Union foundation mable plaque design (Yumbe).png": "14_Miscellaneous",
    "Hearkenth house ministry logo design.png": "14_Miscellaneous",
    "Hopeland High school banner design for Grand Annual Music Dance & Drama Festival 2025.png": "14_Miscellaneous",
    "Jinako Engineering works note book (branding).png": "14_Miscellaneous",
    "Learning Hub Shirt design.png": "14_Miscellaneous",
    "Mak-CAD center projects 2025.png": "14_Miscellaneous",
    "Seinto landscape logo: brand identity .png": "14_Miscellaneous",
    "The Fig tree & vine Foundation Logo design.png": "14_Miscellaneous",
    "Ugandan inpendence Apprel design.png": "14_Miscellaneous",
    "Unicef with support from the Government of netherlands foundation plaque.png": "14_Miscellaneous",
    "Village for every child logo design : brand identity.png": "14_Miscellaneous",
    "millers construction appr.png": "14_Miscellaneous",
    "profile photo_2787 4.JPG": "14_Miscellaneous",
    "rotarct kampala & the polish foundation Africa.png": "14_Miscellaneous"
}

# Step 1: Create all subdirectories inside named/
print("Creating subdirectories...")
for d in dirs.values():
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# Step 2: Move files from root named/ into subdirectories
print("Moving files into their respective subdirectories...")
for file_name, folder in mapping.items():
    src_path = os.path.join(base_dir, file_name)
    dst_path = os.path.join(base_dir, folder, file_name)
    
    if os.path.exists(src_path):
        print(f"Moving: {file_name} -> {folder}/")
        shutil.move(src_path, dst_path)
    else:
        # Check if already moved
        if not os.path.exists(dst_path):
            print(f"Warning: File not found {src_path}")

# Step 3: Rewrite HTML files path references
html_files = ["index.html", "work.html", "blog.html"]

print("Rewriting paths inside HTML files...")
for html_file in html_files:
    if os.path.exists(html_file):
        with open(html_file, "r") as f:
            content = f.read()
        
        # Replace occurrences
        replaced_count = 0
        for file_name, folder in mapping.items():
            # Match "named/filename" or 'named/filename' or named/filename
            old_ref = f"named/{file_name}"
            new_ref = f"named/{folder}/{file_name}"
            
            if old_ref in content:
                content = content.replace(old_ref, new_ref)
                replaced_count += 1
                
        with open(html_file, "w") as f:
            f.write(content)
            
        print(f"Updated {html_file}: replaced {replaced_count} path references.")
    else:
        print(f"Warning: HTML file not found {html_file}")

print("Restructuring successfully completed!")
