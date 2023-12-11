from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu_node.html', takes_context=True)
def draw_menu(context, menu_name):
    
    try:
        all_menus = Menu.objects.all()
        all_menus_value = all_menus.values()
        root_menu = all_menus_value.get(title=menu_name)
        selected_id = int(context['request'].GET[menu_name])
        get_tree(root_menu, all_menus_value, selected_id)
        result_dict = {'menu_nodes' : [root_menu]}
    except:
        result_dict = {
            'menu_nodes': [
                node for node in all_menus.filter(parent_id=None).values()
                ]
            }

    result_dict['menu'] = menu_name
    result_dict['other_querystring'] = get_querystring(context, menu_name)
    return result_dict


def get_tree(root, all_values, selected_id):
    if not root:
        return 
    elif root['menu_id'] == selected_id:
        root['childrens'] = [node for node in all_values.filter(parent_id=root['menu_id'])]
        return root
    else:
        root['childrens'] = list()
        for node in all_values.filter(parent_id=root['menu_id']):
            root['childrens'].append(get_tree(node, all_values, selected_id))      
    return root
            

def get_querystring(context, menu_name):
    querystring_args = []
    for key in context['request'].GET:
        if key != menu_name:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = ('&').join(querystring_args)
    return querystring
    