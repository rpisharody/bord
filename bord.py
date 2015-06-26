#!/usr/bin/python3
"""
    bord - The Board for your website

    bord is a static site generator written in Python 3.
    There are many static site generators like bord.
    This one is mine.

    Written by Rahul Pisharody.
    MIT Licence
"""
import argparse
import os
import re
import time
import markdown
from jinja2 import FileSystemLoader, Environment
import configreader
import server


md = markdown.Markdown()


def mtime(file):
    return time.ctime(os.path.getmtime(file))


def get_cmdline_arguments():
    """
        Function wrapper to parse the input
        arguments provided while invoking bord
    """
    parser = argparse.ArgumentParser(
        description='The Python3 Static Site Generator'
    )
    parser.add_argument(
        "-c", "--config",
        type=str,
        default="~/.bord.rc",
        help="Specify the config file to use"
    )
    parser.add_argument(
        "-s", "--server",
        nargs='?',
        type=int,
        const=8080,
        help="Start a server at the specified port"
    )
    return parser.parse_args()


def create_html(directory, output_directory):
    """
        Convert all markdown files in 'directory'
        into plain HTML format, if the input was changed
    """
    html_dict = {}
    for inputFile in os.listdir(directory):
        post = os.path.join(directory, inputFile)
        output = re.sub('\.md$', '.html', inputFile)
        output = os.path.join(output_directory, output)
        if ( os.path.exists(output) and (mtime(output) > mtime(post)) ):
            pass
        else:
            try:
                f = open(post, 'r', encoding='utf-8')
                html = md.convert(f.read())
                html = render_template(html)
                html_dict[inputFile] = html
                md.reset()
            except IOError as err:
                print('Error while opening', post)
                print('[', err.errno, ']', err.filename, ':', err.strerror)
    return generate_output(html_dict, output_directory)


def render_template(html):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("template.html")
    return template.render(content=html)


def generate_output(html, output_dir):
    count = 0
    try:
        os.makedirs(output_dir)
    except OSError as err:
        print ('Error while creating directory', output_dir)
        print ('[', err.errno, ']', err.filename, ':', err.strerror)

    for inputFile in html:
        outputFile = re.sub('\.md$', '.html', inputFile)
        outputFile = os.path.join(output_dir, outputFile)
        try:
            f = open(outputFile, 'w', encoding='utf-8')
            f.write(html[inputFile])
            f.close()
            count = count + 1
        except IOError as err:
            print (err.strerror)

    return count


def main():
    """
        The main() function of bord.
        Reads/Sets up parameters and calls the
        generate/render methods
    """
    args = get_cmdline_arguments()
    bord_config = configreader.ConfigReader(args.config)
    count = create_html(bord_config['content_dir'], bord_config['output_dir'])
    print ('Created', count, 'HTML files')
    if (args.server):
        print ('Serving at:', str(args.server))
        server.start_server(bord_config['output_dir'], args.server)


if __name__ == '__main__':
    main()
