import requests
from pyecharts import Bar

def get_github_api(url:str)->list:
    '''根据url获得github上获得星数的项目，并存入newdata数组'''
    jsonObj = requests.get(url).json()
    item_dicts = jsonObj['items']
    return [ (dict['name'], dict['stargazers_count']) for dict in item_dicts ]

def draw_chart(data):
    '''将数据用可视化图表进行展现'''
    names, stars = zip(*data)
    bar = Bar('GitHub上星数排名前{}的JavaScript项目'.format(len(names)), height=600, width=1200)
    bar.add('星数', names, stars, xaxis_rotate=30,
            # is_datazoom_show=True, datazoom_type='both', datazoom_range=[0,100],
            mark_line=['average'])
    bar.render(path='github_JavaScript_stars.html')

if __name__ == '__main__':
    # url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
    # draw_chart(get_github_api(url))
    url = 'https://api.github.com/search/repositories?q=language:javascript&sort=star'
    draw_chart(get_github_api(url))