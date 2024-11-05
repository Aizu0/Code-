class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'landslide':
            return '/home/landslide/'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
