import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

nav_link_style = {
    'border-bottom-style': 'solid',
    'border-color': '#b5b8bd',
    'border-width': '1px',
    'padding-left': '15px',
}
nav = dbc.Nav(
    [
        dbc.NavItem(
            dbc.NavLink("Australia",
                        active=True,
                        href="#",
                        style=nav_link_style),
        ),
        dbc.NavItem(dbc.NavLink("People", href="#", style=nav_link_style)),
        dbc.NavItem(dbc.NavLink("Hospital", href="#", style=nav_link_style)),
    ],
    vertical="md",
    navbar=True,
    className='mt-3',
)
