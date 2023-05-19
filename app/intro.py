from dash import html
from dash import dcc

trans_msg = dcc.Markdown(
    """
    **Overview**: Port St. Joe is situated along Highway 98 with Panama City
    to the West and Apalachicola to the East.
    Cecil Costin Sr. Blvd becomes Highway 71 connecting the city to Wewahitchka
    to the Northeast and up to the I-10.
    These main highways support a network of secondary roads running parallel
    and perpendicular to 98.
    
    **Challenges**: Highway 98 runs parallel to the coast and is vulnerable to
    storm flooding.
    Internal secondary roads are at risk from nuisance flooding and completely
    impassable during storms especially near the Bay.
    Residents and visitors may face travel disruptions, lack of reliable
    municipal services, and significant damage to vehicles and other property
    from standing water.
    
    **Value Statement**: Improving the community connections across the City
    of Port St. Joe through effective stormwater management is essential to
    the proper function of the city.
"""
)

comm_msg = dcc.Markdown(
    """
    **Overview**: Port St. Joe’s long history has provided a number of
    community services.
    The city has a historic walkable downtown, schools, numerous churches,
    museums, a library, and other amenities that contribute to the wellbeing
    of its residents.
    These elements contribute to the sense of place that attracts and retains
    a mix of long-term residents, seasonal residents, and visitors to the
    community.
    
    **Challenges**: Hurricane Michael was a wakeup call to the city as damage
    to municipal buildings was substantial.
    Continued growth to the city and surrounding area places additional
    burdens on services.
    The commercial area of Reid Avenue was also badly damaged during the storm
    and, though it has recovered, this area will be at increasing risk with
    sea level rise.
    
    **Value Statement**: Strengthening the network of community services is
    a key to the long-term resilience, including economic prosperity and a
    high quality of life, for residents of the greater community.
"""
)

resrc_msg = dcc.Markdown(
    """
    **Overview**: Port St. Joe is a community surrounded by forestland,
    pasture, and St. Joseph’s Bay. Whether for timber (paper), shipping,
    fishing, scalloping, or tourism, Port St. Joe’s ecosystem services are the
    reason for the city’s long-term prosperity.
    This environment has changed over time as the port and paper mill have
    expanded and contracted and the City has continued to evolve alongside
    these changes.
    
    **Challenges**: Freshwater from the industrial canal and sedimentation has
    led to challenges to water quality in the bay.
    Conversion of forestland to agriculture lands adds additional risk to
    water quality. 
    
    **Value Statement**: Enhancing the ecosystems that support sport fishing,
    scallop habitat, outdoor recreation, and coastal tourism - alongside
    agricultural production and shipping activities - is critical for the
    city’s natural and economic capital.
"""
)

economy_msg = dcc.Markdown(
    """
    **Overview**: Port St. Joe’s mix of industrial, port, and coastal tourism
    provides the city’s economic vitality and community character.
    From earlier times as a port, through years as a mill town, to its current
    condition as a popular vacation spot on the Emerald Coast, Port St. Joe
    has also enabled a vibrant water-based economy.
    
    **Challenges**: The city’s economy has struggled for decades after the
    closing of the St. Joe Paper Company.
    Since then, the Great Recession, Hurricane Michael, and pandemic have
    delivered repeated blows to the economy.
    With increased tidal flooding and storm impacts, economic assets at risk
    include Reid Avenue, the port, marina, and tourism destinations.
    
    **Value Statement**: Maintaining an economic and cultural identity tied to
    the working coast is critical; the city should pursue a diverse array of
    strategies to expand coastal tourism with downtown businesses, boating and
    watersports opportunities, and other economic activities; as well as
    prioritize support for the coastal workforce (such as affordable housing,
    education, etc.).
"""
)

housing_msg = dcc.Markdown(
    """
    **Overview**: Port St. Joe is a former mill town with substantial
    working-class housing stock.
    There are a range of ages, construction types, and price points in PSJ.
    This housing stock traditionally supported a diverse community across race,
    age, and economic status.
    
    **Challenges**: Like many coastal communities in Florida, Port St. Joe has
    seen property values rise substantially in recent years – especially
    following Hurricane Michael – making housing unaffordable to many people.
    Coupled with increased risk from rising tides/coastal flooding and costs
    of upkeep, Port St. Joe’s housing stock is vulnerable to storm damage as
    well as conversion to short-term rental properties.
    
    **Value Statement**: As development pressure increases, Port St. Joe’s
    housing stock should be bolstered and expanded to be more affordable,
    resilient, and diverse in order to support all members of the community.
"""
)

infra_msg = dcc.Markdown(
    """
    **Overview**: Port St. Joe is a small town with a broader industrial
    history and context.
    This resulted in significant investments in in local drinking water, sewer,
    and roadway infrastructure that maintain critical services and functions
    within the City limits.
    Extensive networks of roads, electrical grids, and solid waste facilities
    maintained by the county, state, or other cooperating entities provide
    essential connectivity to services.
    
    **Challenges**: The high level of services have a substantial cost to
    residents leading to high utility and water fees.
    Also, located along the Gulf, PSJ’s infrastructure is always at risk from
    severe storms.
    
    **Value Statement**: Ensuring the continuous functionality of these
    critical services in exceptional flood events is a primary concern for the
    community.
"""
)

overall_msg = dcc.Markdown(
    """
    **What is Critical Asset**: “Critical asset” means an asset whose… loss…
    would result in significant adverse impacts to human life or health,
    national security, or critical economic assets.
    
    **Project Objective**: to assess comprehensive flooding vulnerability and
    create a resilience plan for the City.
    This project is funded by DEP’s Resilient Florida Program and will set
    Cedar Key up to access state infrastructure funds in the coming years to
    address flooding vulnerability.
"""
)

msg_dict = {
    "comm": ["Community Services", comm_msg],
    "infra": ["Critical Infrastructure", infra_msg],
    "resrc": ["Ecosystem Services, Natural & Cultural Resources", resrc_msg],
    "trans": ["Transportation Connectivity", trans_msg],
    "economy": ["Local Economy", economy_msg],
    "housing": ["Affordable Housing", housing_msg],
}


def intro_msg(msg: str = "overall"):
    if msg == "overall":
        return html.Div([overall_msg])
    header = msg_dict[msg][0]
    return html.Div([html.H4(header), msg_dict[msg][1]])
