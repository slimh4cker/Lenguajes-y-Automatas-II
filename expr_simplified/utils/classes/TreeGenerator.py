from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from antlr4.tree.Tree import TerminalNode
import networkx as nx


class TreeGenerator:
    @staticmethod
    def generate_tree_image(tree, parser):
        try:
            G = nx.DiGraph()
            pos = {}
            labels = {}

            def build_graph(parent, node, depth=0, pos_x=0.5, width=1.0):
                if node is None:
                    return 0
                if isinstance(node, TerminalNode):
                    label = node.getText()
                else:
                    label = parser.ruleNames[node.getRuleIndex()]

                node_id = id(node)
                G.add_node(node_id)
                labels[node_id] = label

                # Get pos
                pos[node_id] = (pos_x, -depth)

                if parent is not None:
                    G.add_edge(parent, node_id)

                children = list(node.getChildren()) if not isinstance(node, TerminalNode) else []
                n = len(children)
                if n > 0:
                    child_width = width / n
                    for i, child in enumerate(children):
                        build_graph(node_id, child, depth + 1,
                                    pos_x - width / 2 + i * child_width + child_width / 2,
                                    child_width)

                return 1

            # Tree Structure
            build_graph(None, tree)
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.set_facecolor('#2b2d4f')
            fig.set_facecolor('#2b2d4f')

            # Draw edges
            for edge in G.edges():
                x1, y1 = pos[edge[0]]
                x2, y2 = pos[edge[1]]
                ax.plot([x1, x2], [y1, y2], color='#dcdcdc', linewidth=1.5, zorder=1)

            # Draw nodes
            for node in G.nodes():
                x, y = pos[node]
                ax.add_patch(Circle((x, y), 0.08, color='#6a5acd', zorder=2))
                ax.text(x, y, labels[node],
                        ha='center', va='center',
                        color='white',
                        fontsize=8,
                        bbox=dict(facecolor='#6a5acd', edgecolor='none', boxstyle='round,pad=0.2'))

            ax.axis('off')
            plt.tight_layout()

            buf = BytesIO()
            plt.savefig(buf, format='png', facecolor=fig.get_facecolor(), dpi=100)
            plt.close()
            buf.seek(0)

            return buf

        except Exception as e:
            print(f"Error generating tree: {e}")
            return None