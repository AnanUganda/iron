import os
import json

base_dir = "named"
manifest_path = "projects-manifest.json"

# Project metadata configurations
metadata = {
    "01_His_Image_Ministries": {
        "name": "His Image Ministries (HIM)",
        "category": "Brand Identity / NGO",
        "description": "Comprehensive visual identity and campaign systems for East African outreach. This suite includes reflector apparel, silicon wristbands, signposts, and extensive trifold brochures outlining singlehood, marriage, and community health initiatives."
    },
    "02_Makerere_AI_Lab_M_vet": {
        "name": "Makerere AI Lab & M-vet",
        "category": "UI / Web Design & Machine Learning",
        "description": "High-fidelity UI graphics, infographics, certificates, and academic banners designed for the Mobile Veterinary Diagnostics (M-VET) and Automated Speech Translation initiatives. This includes visual assets for livestock dataset diagnostic hackathons."
    },
    "03_Ekijul_Real_Estate": {
        "name": "Ekijul Real Estate & Developers",
        "category": "Brand Design & Identity",
        "description": "Premium brand design for a premier real estate development firm in Uganda. Features clean typographic logos, branded industrial safety wear (construction helmets), corporate caps, notebook stationery, and keyholder mockups."
    },
    "04_Kazo_Technical_School": {
        "name": "Kazo Technical School",
        "category": "Advertising & Print Campaign",
        "description": "Academic promotion suite designed to expand enrollment and drive registrations. Includes physical awards plaques, teardrop advertising banners, roadside rollup banners, vehicular stickers, and strategic enrollment brochures."
    },
    "05_Tukue_Pamoja": {
        "name": "Tukue Pamoja",
        "category": "Brand Identity & Apparel",
        "description": "Corporate branding elements showcasing unity and community strength. Features apparel sweater-shirts, corporate business cards, and layout elements on trifold marketing brochures."
    },
    "06_Morgan_Concrete_Services": {
        "name": "Morgan Concrete Services",
        "category": "Brand Design / Industrial",
        "description": "Heavy-duty industrial corporate brand suite tailored for civil engineering and concrete suppliers. Features heavy vehicle stickers, concrete mixer hood wraps, and premium concrete corporate apparel."
    },
    "07_Sawers_Harvest_Cafe": {
        "name": "Sawers Harvest Cafe",
        "category": "Brand & Packaging Design",
        "description": "Artisanal beverage startup branding based in Kampala. Features premium eco-friendly coffee cup patterns, custom beverage bottles, and rich typographic logo variations for local cafe placement."
    },
    "08_Inspire_Coffee": {
        "name": "Inspire Coffee Digital Fund",
        "category": "UI / Web Design",
        "description": "User experience mapping and interface visual designs for a digital coffee funding network. Features interactive web layout mockups, high-fidelity app screens, and custom roadside promotional rollup banners."
    },
    "09_Zion_Shelter": {
        "name": "Zion Shelter",
        "category": "Advertising & NGO Outreach",
        "description": "Social impact design systems supporting family logistics and shelter initiatives. Features laptop stickers, Christmas charity flyer drives, and user registration application forms."
    },
    "10_Antioch_Resource_Center": {
        "name": "Antioch Christian Resource Center",
        "category": "Advertising Design",
        "description": "Strategic promotional campaigns and outdoor posters designed to expand community access to inductive Bible courses and regional workshops."
    },
    "11_Willowhill_Golden_Doodles": {
        "name": "Willowhill Golden Doodles",
        "category": "Brand Design / Identity",
        "description": "Elegant pet-breeder visual identity suite, featuring corporate typographic logos and visual assets designed to reflect warmth and credibility."
    },
    "12_Mbarara_Junior_School": {
        "name": "Mbarara Junior School",
        "category": "Branding & Print",
        "description": "Cohesive primary school branding features, including beautifully illustrated exercise book covers, class timetables, and creative academic stationery layouts."
    },
    "13_Medium_Blog_Articles": {
        "name": "Medium Blog Articles",
        "category": "Editorial & Insights",
        "description": "Samson's published articles exploring the intersection of modern visual design, biomimicry, animal-inspired interfaces (waggle dance, cats eyes), first responder logistics, and design strategy."
    },
    "14_Miscellaneous": {
        "name": "Miscellaneous & Collaborations",
        "category": "Design Collection",
        "description": "A collection of individual visual pieces, campaign posters, national celebrations (Uganda Independence apparel), FRC brand logos, and cooperative foundation plaques designed for UNICEF, Netherlands Embassy, and Rotaract Kampala."
    }
}

manifest = {}

# Scan named/ directory
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    if os.path.isdir(folder_path):
        # Gather all files in this folder
        files = []
        for file in os.listdir(folder_path):
            if not file.startswith('.'): # skip DS_Store
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    files.append(file)
        
        # Sort files by name
        files.sort()
        
        # Build project entry
        project_id = folder_name
        proj_meta = metadata.get(project_id, {
            "name": project_id.replace("_", " "),
            "category": "Design Work",
            "description": f"Design files for project {project_id}."
        })
        
        manifest[project_id] = {
            "id": project_id,
            "name": proj_meta["name"],
            "category": proj_meta["category"],
            "description": proj_meta["description"],
            "files": [f"named/{project_id}/{f}" for f in files]
        }

# Write out manifest JSON
with open(manifest_path, "w") as out:
    json.dump(manifest, out, indent=2)

print(f"Manifest written successfully to {manifest_path} with {len(manifest)} projects.")
