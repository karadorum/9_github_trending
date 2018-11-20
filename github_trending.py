import requests
import pprint
import datetime


def get_date_before_today(num_of_days):
    current_date = datetime.date.today()
    ago = datetime.timedelta(days=num_of_days)
    date_delta = current_date - ago
    return date_delta


def get_trending_repositories(request_date):
    github_search_url = 'https://api.github.com/search/repositories'
    creation_date = 'created:>={}'.format(request_date)
    request_args = {'q': creation_date, 'sort': 'stars'}
    response = requests.get(github_search_url, params=request_args)
    trending_repos = response.json()['items']
    return trending_repos


def print_repo_info(repo_list):
    for repo in repo_list:
        repo_url = repo['html_url']
        repo_stars = repo['stargazers_count']
        repo_issues = repo['open_issues']
        print('url: {}, stars: {} open issues: {}'.format(
            repo_url,
            repo_stars,
            repo_issues))


if __name__ == '__main__':
    days_before = 7
    max_repos_amount = 20
    trending_repos = get_trending_repositories(
        get_date_before_today(days_before))[:max_repos_amount]
    print_repo_info(trending_repos)
