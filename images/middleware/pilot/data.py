def stage_in(source,target):
    print('downloading {} to {}'.format(source,target))
    with open(target,'w') as out:
        out.write('contents of {} in {}'.format(source,target))

def stage_out(source,target):
    print('uploading {} to {}'.format(source,target))
    with open(source,'r') as src:
        print('--- stage out content begin ---')
        print(src.read())
        print('--- stage out content end ---')
        