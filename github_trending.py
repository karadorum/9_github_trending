import requests
import pprint
import datetime


def get_date_before_today(num_of_days):
    current_date = datetime.date.today()
    ago = datetime.timedelta(days=num_of_days)
    date_delta = current_date - ago
    return date_delta


def get_trending_repositories(request_date, max_repos_amount=20):
    github_search_url = 'https://api.github.com/search/repositories'
    creation_date = 'created:>={}'.format(request_date)
    request_args = {'q': creation_date, 'sort': 'stars'}
    response = requests.get(github_search_url, params=request_args)
    trending_repos = response.json()['items']
    return trending_repos[:max_repos_amount]


def get_repo_issues(repo_name):
    url = 'https://api.github.com/repos/{}/issues'.format(repo_name)
    response = requests.get(url)
    open_issues_list = response.json()
    open_issues_num = len(
        [repo_issue for repo_issue in open_issues_list if 'pull_request' not in repo_issue])
    return open_issues_num


if __name__ == '__main__':
    days_before = 7
    trending_repos = get_trending_repositories(
        get_date_before_today(days_before))
    for repo in trending_repos:
        repo_url = repo['html_url']
        repo_stars = repo['stargazers_count']
        repo_issues = get_repo_issues(repo['full_name'])
        print('url: {}, stars: {} open issues: {}'.format(
            repo_url,
            repo_stars,
            repo_issues))
