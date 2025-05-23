import pandas as pd

def parse_analysis_dataframe(data):
    analysis_df = pd.json_normalize(
        data,
        record_path=['education'],
        meta=['name', ['contact', 'phone'], ['contact', 'email']],
        errors='ignore'
    )
    analysis_df.rename(columns={
        'contact.phone': 'phone',
        'contact.email': 'email'
    }, inplace=True)
    cols = ['name'] + [col for col in analysis_df.columns if col != 'name']
    return analysis_df[cols]

def parse_summary_dataframe(data):
    education_bullets = "\n".join([
        f"- {edu['degree']} at {edu['institution']} (GPA: {edu.get('gpa', 'N/A')})"
        for edu in data["education"]
    ])
    return pd.DataFrame([{
        "Name": data["name"],
        "Phone": data["contact"]["phone"],
        "Email": data["contact"]["email"],
        "Education": education_bullets
    }])
