import click
import json
import os

@click.command()
@click.option('-s', '--sort-by', type = click.STRING, help = 'Output to be sorted by this field (id by default).')
@click.option('-c', '--count', default = 10, type = click.INT, help = 'Number of bookmarks to be listed (10 by default).')
@click.option('-t', '--tag', type = click.STRING, help = 'List bookmarks containing the specified tag.')
def show(count, sort_by, tag):
    
    '''Shows all currently saved bookmarks'''
    
    #Expand the '~' to the user's home directory
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        objects = json.loads(f.read())
    
    #Filter out the bookarks which contain the tag
    if tag:
        tag = tag.lower()
        objects = filter(lambda x: tag in [y.lower() for y in x['tags']], objects)
        objects = list(objects)
    
    #Sort the list of objects by the key as specified
    if sort_by:
        objects = sorted(objects, key = lambda k: k[sort_by])
    
    #Set number of objects to be displayed to the count
    objects = objects[0:count]
    
    #First line of output describes the options provided   
    output_string = 'Listing {0} bookmarks'.format(count)
    if tag:
        output_string += ' tagged "{0}"'.format(tag)
    if sort_by:
        output_string += ' sorted by "{0}"'.format(sort_by)
    output_string += ':\n'
    click.echo(output_string)
    #Display only the name and url
    for x in objects:
        click.echo('{0}:\t{1}'.format(x['name'], x['url']))