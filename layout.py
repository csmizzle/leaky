from app_tools.graphs import draw_bubble_map
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd


email_count = pd.read_csv('./app_data/email_count.csv')
state_email = pd.read_csv('./app_data/city_phone.csv')
loc_data = pd.read_csv('./app_data/map_data.csv')

layout = dbc.Container([
    html.H1('Facebook 2021 Data Breach'),
    dbc.Card([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.H4("Background"),
                    html.Hr(),
                    dcc.Markdown("Early on April 3rd, 2021 approximately 553 million Facebook accounts were leaked online."
                             " Accounts from around the globe are effected in this breach,"
                             " along with 32 million from the United States. The dataset includes phone number,"
                             " date of birth, first name, last name, location (city, state), email address, employer, and gender"
                             " with varying degrees of completion based on the corresponding Facebook page."),
                    dcc.Markdown("In September 2019, [Motherboard](https://www.vice.com/en/article/xgz7bd/facebook-phone-numbers-bot-telegram) reported"
                             " on a Telegram bot that takes a phone number as input and looks the corresponding Facebook profile."
                             " This was discovered as a vulnerability by Facebook, fixing the vulnerability by"
                             " early Aug 2019. The data's legitimacy was also confirmed by Motherboard in the same report."),
                    dcc.Markdown("While the exact source of the vulnerability cannot be determined, it is likely tied"
                             " to a [similar vulnerability](https://www.forbes.com/sites/zakdoffman/2019/09/12/new-instagram-hack-exclusive-facebook-confirms-user-accounts-and-phone-numbers-at-risk/?sh=7b2f5b482200),"
                             " first identified by @ZHacker13 (ZH), targeting Instagram account creation and contact syncing."
                             " It should be noted that Facebook owns Instagram."
                             " ZH notified Facebook of the vulnerability in early August 2019 and Facebook confirmed"
                             " the existence of the vulnerability but deemed it low risk. A month later Facebook changed"
                             " their stance, deeming it a serious security flaw. At the time, it seemed there"
                             " had been no serious data leakage due to the vulnerability."),
                    dcc.Markdown("Alon Gal, a respected figure head in the Twitter Security Community,"
                             " posted [screen shots](https://twitter.com/UnderTheBreach/status/1349671417625931778?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1349671417625931778%7Ctwgr%5E%7Ctwcon%5Es1_c10&ref_url=https%3A%2F%2Fwww.theverge.com%2F2021%2F1%2F25%2F22249571%2Ffacebook-phone-number-hack-telegram-bot)"
                             " in early January 2021 detailing a breach of approximately 553 million Facebook accounts"
                             " with similar fields that were extracted in the Instagram vulnerability."
                             "Now, the previously 553 million payment protected"
                             " records are available for free. The accompanying data revolves only around the 32 million US accounts.")
                ])
            ]),
            dbc.Col(
                dcc.Graph(
                    figure=draw_bubble_map(loc_data),
                )
            )

        ]),
    ], body=True),

    html.Br(),

    dbc.Card([
        html.H4("Searchable Breached Email Domains"),

        html.Hr(),

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                    id='email-count-table',
                    columns=[
                        {'name': 'Email Domain', 'id': 'email_domain'},
                        {'name': 'Count (filter with >, <, =, etc.)', 'id': 'count'}
                    ],
                    data=email_count.to_dict('records'),
                    filter_action='native',
                    sort_action="native",
                    sort_mode="multi",
                    style_table={
                        'height': 400,
                    },
                    style_data={
                        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                    },
                    page_size=10
                )
            ),

            dbc.Col(
                dash_table.DataTable(
                    id='email-state-count-table',
                    columns=[
                        {'name': 'City, State', 'id': 'location_1'},
                        {'name': 'Email Domain', 'id': 'email_domain'},
                        {'name': 'Count (filter with >, <, =, etc.)', 'id': 'count'}
                    ],
                    data=state_email.to_dict('records'),
                    filter_action='native',
                    sort_action="native",
                    sort_mode="multi",
                    style_table={
                        'height': 400,
                    },
                    style_data={
                        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                    },
                    page_size=10
                )
            ),
        ])
    ], body=True),
], fluid=True)
