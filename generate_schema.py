import json

# Initialize an empty dictionary to store schema data
schema_data = {}

# Function to validate URL
def validate_url(url):
    # Add URL validation logic here
    return url

# Basic Information
schema_data["@type"] = input("Enter the type of your local business (e.g., Medical Clinic): ")
schema_data["name"] = input("Enter the name of your business: ")
schema_data["url"] = validate_url(input("Enter the URL of your business website: "))
schema_data["telephone"] = input("Enter the telephone number for your business: ")

# Knows About (Entities)
knows_about_count = int(input("How many 'knowsAbout' entities do you want to add? "))
knows_about_urls = [validate_url(input(f"Enter a URL for entity {i+1}: ")) for i in range(knows_about_count)]
schema_data["knowsAbout"] = knows_about_urls

# Social Media and Citations
same_as_count = int(input("How many social media profiles and citations do you want to add? "))
same_as = [validate_url(input(f"Enter URL {i+1}: ")) for i in range(same_as_count)]
schema_data["sameAs"] = same_as

# Media
schema_data["logo"] = validate_url(input("Enter the URL of your business logo: "))
schema_data["image"] = validate_url(input("Enter an image URL from your website or Google Business Profile: "))

# Description and Keywords
schema_data["description"] = input("Enter a description of your business: ")
schema_data["keywords"] = input("Enter keywords related to your business (comma-separated): ")

# Alternate Names
alternate_names_count = int(input("How many alternate names does your business have? "))
alternate_names = [input(f"Enter alternate name {i+1}: ") for i in range(alternate_names_count)]
schema_data["alternateName"] = alternate_names

# Address and Geo-Coordinates
address = {
    "@type": "PostalAddress",
    "streetAddress": input("Enter the street address of your business: "),
    "addressLocality": input("Enter the locality your business is in: "),
    "addressRegion": input("Enter the region your business is in: "),
    "postalCode": input("Enter the postal code of your business: "),
    "addressCountry": input("Enter the country your business is in: ")
}
schema_data["address"] = address

# Geo-Coordinates
geo = {
    "@type": "GeoCoordinates",
    "latitude": input("Enter the latitude of your business location: "),
    "longitude": input("Enter the longitude of your business location: ")
}
schema_data["geo"] = geo

# Hours of Operation
day_of_week = input("Enter a day of the week your business is open (e.g., Monday): ")
opens = input(f"Enter the opening time on {day_of_week} (e.g., 09:00): ")
closes = input(f"Enter the closing time on {day_of_week} (e.g., 17:00): ")
schema_data["openingHoursSpecification"] = [{"@type": "openingHoursSpecification", "dayOfWeek": day_of_week, "opens": opens, "closes": closes}] * 7

# Additional Information
schema_data["priceRange"] = input("Enter the price range of your services (e.g., $$$): ")

# Aggregate Rating
schema_data["aggregateRating"] = {
    "@type": "AggregateRating",
    "ratingValue": input("Enter your average rating on Google My Business: "),
    "ratingCount": input("Enter the total number of reviews on Google My Business: ")
}

# Offer Catalog
offers = []
for i in range(5):
    offer = {
        "@type": "Offer",
        "name": input(f"Enter the name of offer {i+1}: "),
        "description": input(f"Enter the description of offer {i+1}: "),
        "price": input(f"Enter the price of offer {i+1}: "),
        "priceCurrency": input(f"Enter the currency of offer {i+1} (e.g., USD): "),
        "availability": input(f"Enter the availability of offer {i+1} (e.g., InStock, OutOfStock): ")
    }
    offers.append(offer)

schema_data["hasOfferCatalog"] = {
    "@type": "OfferCatalog",
    "name": "Catalog of Services",
    "itemListElement": offers
}

# FAQs
faqs_count = int(input("How many FAQs do you want to add? "))
faqs = [{"@type": "Question", "name": input(f"Enter question {i+1}: "), "acceptedAnswer": {"@type": "Answer", "text": input(f"Enter answer for question {i+1}: ")}} for i in range(faqs_count)]
schema_data["mainEntity"] = [{"@type": "FAQPage", "mainEntity": faqs}]

# Reviews
reviews_count = int(input("How many reviews do you want to add? "))
reviews = [{"@type": "Review", "author": input(f"Enter author of review {i+1}: "), "reviewBody": input(f"Enter body of review {i+1}: "), "reviewRating": {"@type": "Rating", "ratingValue": input(f"Enter rating of review {i+1} (1-5): ")}} for i in range(reviews_count)]
schema_data["review"] = reviews

# Output the schema data in JSON-LD format
print("\nGenerated Schema Data in JSON-LD Format:")
print(json.dumps(schema_data, indent=4))
