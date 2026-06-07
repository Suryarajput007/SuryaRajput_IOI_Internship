print("=" * 60)
print("📄 AI RESUME SCREENING ASSISTANT")
print("=" * 60)

required_skills = {
    "python": 20,
    "java": 15,
    "sql": 15,
    "machine learning": 25,
    "communication": 10,
    "teamwork": 5,
    "problem solving": 10
}

resume = input("\nPaste Resume Text:\n\n").lower()

score = 0
matched_skills = []
missing_skills = []

for skill, points in required_skills.items():
    if skill in resume:
        score += points
        matched_skills.append(skill.title())
    else:
        missing_skills.append(skill.title())

print("\n" + "=" * 60)
print("📊 RESUME ANALYSIS REPORT")
print("=" * 60)

print(f"\n✅ Skills Found ({len(matched_skills)}):")
for skill in matched_skills:
    print("   •", skill)

print(f"\n❌ Missing Skills ({len(missing_skills)}):")
for skill in missing_skills:
    print("   •", skill)

print(f"\n🎯 Overall Resume Score: {score}/100")

if score >= 80:
    status = "🏆 Highly Recommended"
elif score >= 60:
    status = "✅ Shortlisted"
elif score >= 40:
    status = "⚠️ Consider for Interview"
else:
    status = "❌ Not Shortlisted"

print(f"\n📌 Candidate Status: {status}")

print("\n💡 Recommendations:")

if missing_skills:
    print("   Improve the following skills:")
    for skill in missing_skills:
        print("   -", skill)
else:
    print("   Excellent profile! All required skills detected.")

print("\n" + "=" * 60)
print("Screening Completed Successfully!")
print("=" * 60)