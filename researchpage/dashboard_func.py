from researchpage.dashboard.gpt_classifier import gpt_classifier
from researchpage.dashboard.ipc_category_graph import ipc_category_graph
from researchpage.dashboard.ipc_subcategory_graph import ipc_subcategory_graph

def create_dashboard(user_input: str) -> str:
    code = gpt_classifier(user_input)
    ipc_category = code[1]
    ipc_category_graph_image = ipc_category_graph(ipc_category)
    ipc_subcategory_graph_image = ipc_subcategory_graph(code[1:-1])

    return ipc_category_graph_image, ipc_subcategory_graph_image