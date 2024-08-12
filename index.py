# ⚠️ USE AT YOUR OWN RISK
# first: pip install pysqlite3-binary
# then in settings.py:

# these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
# import os
# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
import chromadb
import requests
from flask import Flask
import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension

app = Flask(__name__)
@app.route('/')
def hello_world():
    initDb()
    results = getResults('how does my project use the Select decorator to access one of my states')
    response = getChatGptResponse(results)
    print(response)
    return response

global collection
def initDb():
    global collection
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection", get_or_create=True)
    collection.add(
        documents=[
            "Import necessary Angular core components, RxJS operators, and other dependencies.",
            "Define an interface for the sidebar state to maintain consistency and type safety.",
            "Component decorator that defines the selector, template URL, stylesheet URL, and change detection strategy for the component.",
            "SecuredSidebarComponent class definition that implements the OnInit lifecycle hook.",
            "Select the current user state from the NGXS store.",
            "Bind the 'open' CSS class to the component based on the _opened property.",
            "Input property to set the sidebar title, defaults to 'SeedMC'.",
            "Input property to toggle the sidebar's open state.",
            "Input property to set the sidebar's menu items.",
            "Output event emitter to notify when the sidebar is toggled.",
            "Define the initial state of the sidebar.",
            "ReplaySubject to manage and emit partial updates to the sidebar's state.",
            "Observable that emits the current state of the sidebar.",
            "Observable that tracks the sidebar's open state.",
            "Observable that tracks the arrow icon type based on the sidebar's open state.",
            "Observable that emits the list of menu items in the sidebar.",
            "Constructor injecting Angular's Router and NGXS Store services.",
            "Lifecycle hook to handle any initialization logic.",
            "Method to toggle the sidebar's open state and navigate to a specific route if provided.",
            "Method to expand a specific menu item in the sidebar.",
            "Method placeholder for handling notifications.",
            "Method to log the user out by dispatching the LogoutAction to the NGXS store."
        ],
        metadatas=[
                    {
                        "description": "Import necessary Angular core components, RxJS operators, and other dependencies.",
                        "code": "import {ChangeDetectionStrategy, Component, EventEmitter, HostBinding, Input, OnInit, Output} from '@angular/core';\nimport {coerceBooleanProperty} from '@angular/cdk/coercion';\nimport {Observable, ReplaySubject} from 'rxjs';\nimport {distinctUntilChanged, map, scan, shareReplay, tap} from 'rxjs/operators';\nimport {MenuItem, User} from '@smc/ui-common';\nimport {Router} from '@angular/router';\nimport { Select, Store } from '@ngxs/store';\nimport { LogoutAction, UserState } from '@smc/ui-state';"
                    },
                    {
                        "description": "Define an interface for the sidebar state to maintain consistency and type safety.",
                        "code": "interface SidebarState {\n  arrowType: string;\n  opened: boolean;\n  menuItems: MenuItem[];\n  expandedItem: MenuItem | null;\n  tooltipDelay: number;\n}"
                    },
                    {
                        "description": "Component decorator that defines the selector, template URL, stylesheet URL, and change detection strategy for the component.",
                        "code": "@Component({\n  selector: 'smc-secured-sidebar',\n  templateUrl: './secured-sidebar.component.html',\n  styleUrls: ['./secured-sidebar.component.scss'],\n  changeDetection: ChangeDetectionStrategy.OnPush\n})"
                    },
                    {
                        "description": "SecuredSidebarComponent class definition that implements the OnInit lifecycle hook.",
                        "code": "export class SecuredSidebarComponent implements OnInit {"
                    },
                    {
                        "description": "Select the current user state from the NGXS store.",
                        "code": "  @Select(UserState.user)\n  public user$!: Observable<User>;"
                    },
                    {
                        "description": "Bind the 'open' CSS class to the component based on the _opened property.",
                        "code": "  @HostBinding('class.open')\n  private get _opened(): boolean {\n    let val: boolean;\n    this.opened$.subscribe(opened => (val = opened));\n    return val;\n  }"
                    },
                    {
                        "description": "Input property to set the sidebar title, defaults to 'SeedMC'.",
                        "code": "  @Input()\n  public title: string = 'SeedMC';"
                    },
                    {
                        "description": "Input property to toggle the sidebar's open state.",
                        "code": "  @Input()\n  public set opened(value: boolean) {\n    this._state.next({opened: coerceBooleanProperty(value)});\n  }"
                    },
                    {
                        "description": "Input property to set the sidebar's menu items.",
                        "code": "  @Input()\n  public set menuItems(value: MenuItem[]) {\n    if (!Array.isArray(value)) {\n      value = [];\n    }\n    this._state.next({menuItems: value});\n  }"
                    },
                    {
                        "description": "Output event emitter to notify when the sidebar is toggled.",
                        "code": "  @Output()\n  public toggle: EventEmitter<boolean | void> = new EventEmitter<boolean | void>();"
                    },
                    {
                        "description": "Define the initial state of the sidebar.",
                        "code": "  private _initialState: SidebarState = {\n    arrowType: 'arrow-alt-from-left',\n    opened: false,\n    menuItems: [],\n    expandedItem: null,\n    tooltipDelay: 500\n  };"
                    },
                    {
                        "description": "ReplaySubject to manage and emit partial updates to the sidebar's state.",
                        "code": "  private _state: ReplaySubject<Partial<SidebarState>>\n    = new ReplaySubject<Partial<SidebarState>>();"
                    },
                    {
                        "description": "Observable that emits the current state of the sidebar.",
                        "code": "  public state$: Observable<SidebarState> = this._state.asObservable().pipe(\n    scan(\n      (sidebarState: SidebarState, command: Partial<SidebarState>): SidebarState => ({...sidebarState, ...command}),\n      this._initialState\n    ),\n    shareReplay(1)\n  );"
                    },
                    {
                        "description": "Observable that tracks the sidebar's open state.",
                        "code": "  public opened$: Observable<boolean> = this.state$.pipe(\n    map(data => data.opened),\n    distinctUntilChanged(),\n    tap(opened =>\n      this._state.next({arrowType: opened ? 'chevron_left' : 'chevron_right'})\n    )\n  );"
                    },
                    {
                        "description": "Observable that tracks the arrow icon type based on the sidebar's open state.",
                        "code": "  public arrowIcon$: Observable<string> = this.state$.pipe(\n    map(data => data.arrowType),\n    distinctUntilChanged()\n  );"
                    },
                    {
                        "description": "Observable that emits the list of menu items in the sidebar.",
                        "code": "  public menuItems$: Observable<MenuItem[]> = this.state$.pipe(\n    map(data => data.menuItems),\n    distinctUntilChanged()\n  );"
                    },
                    {
                        "description": "Constructor injecting Angular's Router and NGXS Store services.",
                        "code": "  constructor(\n    private router: Router,\n    private _store: Store\n  ) {\n  }"
                    },
                    {
                        "description": "Lifecycle hook to handle any initialization logic.",
                        "code": "  ngOnInit(): void {\n  }"
                    },
                    {
                        "description": "Method to toggle the sidebar's open state and navigate to a specific route if provided.",
                        "code": "  public toggleOpen(state: SidebarState, route?: string): void {\n    if (route) {\n      this.router.navigateByUrl(route);\n    }\n    this.toggle.emit();\n  }"
                    },
                    {
                        "description": "Method to expand a specific menu item in the sidebar.",
                        "code": "  public expandItem(opened: boolean, expandedItem: MenuItem | null, item: MenuItem): void {\n    if (!opened) {\n      this.toggle.emit(true);\n    }\n    this._state.next({expandedItem: !opened || item?.id !== expandedItem?.id ? item : null});\n  }"
                    },
                    {
                        "description": "Method placeholder for handling notifications.",
                        "code": "  public notifications(): void {\n    //console.log('notifications');\n  }"
                    },
                    {
                        "description": "Method to log the user out by dispatching the LogoutAction to the NGXS store.",
                        "code": "  public logout(): void {\n    //console.log('logout');\n    this._store.dispatch(new LogoutAction(false, false));\n  }\n}"
                    }
        ],
        ids=[
            "desc_001",
            "desc_002",
            "desc_003",
            "desc_004",
            "desc_005",
            "desc_006",
            "desc_007",
            "desc_008",
            "desc_009",
            "desc_010",
            "desc_011",
            "desc_012",
            "desc_013",
            "desc_014",
            "desc_015",
            "desc_016",
            "desc_017",
            "desc_018",
            "desc_019",
            "desc_020",
            "desc_021",
            "desc_022"
        ]

    )

def getResults(query: str):
    global collection
    print("query results: ", query)
    return collection.query(
        query_texts=[query],
        n_results=2,
    )

def getChatGptResponse(results):
    # Your API key here
    api_key = "sk-proj-cgDZq9Elx5aVo6FpboEnT3BlbkFJbjiqOKm1j6MtF6Weq1nh"

    # The endpoint you want to use, e.g., for chat completions
    url = "https://api.openai.com/v1/chat/completions"

    # The headers for authentication and content type
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    providedContext = ''
    for codeChunk in results['metadatas'][0]:
        providedContext += codeChunk['code'] + '\n\n'

    # print(f'context is {providedContext}')
    prompt="How do I Select the users State?"
    # The data for the request
    data = {
        "model": "gpt-4o",  # Specify the model you want to use
        "messages": [
            {"role": "system", "content": "You are helping generate code for an angular typecript component."},
            
            {"role": "user", "content": f'If these contexts are related, reference them {providedContext}'},
            {"role": "user", "content": prompt}
        ]
    }

    # Make the POST request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response from the API
        return markdown.markdown(response.json()['choices'][0]['message']['content'].replace("```", "\n\n"), extensions=[TableExtension(), FencedCodeExtension()])
    else:
        # Print the error if the request failed
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    