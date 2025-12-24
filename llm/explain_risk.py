def explain_disaster_risk(disaster, risk):

    risk = str(risk).lower()  # normalize output

    # ================= FLOOD =================
    if disaster == "Flood":
        if risk in ["high", "very_high"]:
            return (
                "🌊 FLOOD – HIGH RISK\n\n"
                "Situation:\n"
                "Very heavy rainfall and poor drainage may cause severe flooding.\n\n"
                "Citizen Actions:\n"
                "- Move to higher ground immediately\n"
                "- Avoid flooded roads and bridges\n"
                "- Keep emergency kit and documents ready\n\n"
                "Authority Actions:\n"
                "- Deploy rescue and relief teams\n"
                "- Open flood relief shelters\n"
                "- Issue continuous public flood alerts"
            )

        elif risk == "moderate":
            return (
                "🌊 FLOOD – MODERATE RISK\n\n"
                "Situation:\n"
                "Increased rainfall may cause waterlogging in low-lying areas.\n\n"
                "Citizen Actions:\n"
                "- Avoid low-lying areas\n"
                "- Stay alert to weather updates\n\n"
                "Authority Actions:\n"
                "- Monitor drainage systems\n"
                "- Keep emergency teams on standby"
            )

        else:
            return (
                "🌊 FLOOD – LOW RISK\n\n"
                "Citizen Actions:\n"
                "- Stay informed through local advisories\n\n"
                "Authority Actions:\n"
                "- Continue routine monitoring"
            )

    # ================= EARTHQUAKE =================
    elif disaster == "Earthquake":
        if risk in ["high", "orange", "red"]:
            return (
                "🌋 EARTHQUAKE – HIGH RISK\n\n"
                "Situation:\n"
                "Seismic indicators suggest a high impact earthquake risk.\n\n"
                "Citizen Actions:\n"
                "- Stay away from weak or old structures\n"
                "- Secure heavy furniture\n"
                "- Keep emergency supplies ready\n\n"
                "Authority Actions:\n"
                "- Issue seismic risk alerts\n"
                "- Inspect critical infrastructure\n"
                "- Prepare emergency response units"
            )

        elif risk in ["yellow", "moderate"]:
            return (
                "🌋 EARTHQUAKE – MODERATE RISK\n\n"
                "Situation:\n"
                "Moderate seismic activity detected.\n\n"
                "Citizen Actions:\n"
                "- Stay alert and follow safety drills\n\n"
                "Authority Actions:\n"
                "- Increase seismic monitoring\n"
                "- Alert disaster response teams"
            )

        else:
            return (
                "🌋 EARTHQUAKE – LOW RISK\n\n"
                "Citizen Actions:\n"
                "- Stay aware of safety procedures\n\n"
                "Authority Actions:\n"
                "- Continue routine seismic monitoring"
            )

    # ================= CYCLONE =================
    elif disaster == "Cyclone":
        if risk in ["high", "very_high"]:
            return (
                "🌪️ CYCLONE – HIGH RISK\n\n"
                "Situation:\n"
                "Atmospheric conditions strongly favor cyclone formation.\n\n"
                "Citizen Actions:\n"
                "- Secure homes and loose objects\n"
                "- Avoid coastal and low-lying areas\n"
                "- Follow evacuation instructions\n\n"
                "Authority Actions:\n"
                "- Issue cyclone warnings\n"
                "- Evacuate vulnerable coastal zones\n"
                "- Deploy disaster response forces"
            )

        elif risk == "moderate":
            return (
                "🌪️ CYCLONE – MODERATE RISK\n\n"
                "Situation:\n"
                "Weather conditions show potential cyclone development.\n\n"
                "Citizen Actions:\n"
                "- Stay updated with weather alerts\n\n"
                "Authority Actions:\n"
                "- Monitor wind and pressure trends\n"
                "- Prepare emergency response teams"
            )

        else:
            return (
                "🌪️ CYCLONE – LOW RISK\n\n"
                "Citizen Actions:\n"
                "- Stay informed through official advisories\n\n"
                "Authority Actions:\n"
                "- Continue meteorological monitoring"
            )

    # ================= DEFAULT =================
    else:
        return "No disaster risk explanation available."
