from dataloaders.datasets import landslide
from torch.utils.data import DataLoader

def make_data_loader(args, **kwargs):

    if args.dataset == 'pascal':
        train_set = pascal.VOCSegmentation(args, split='train')
        val_set = pascal.VOCSegmentation(args, split='val')
        if args.use_sbd:
            sbd_train = sbd.SBDSegmentation(args, split=['train', 'val'])
            train_set = combine_dbs.CombineDBs([train_set, sbd_train], excluded=[val_set])

        num_class = train_set.NUM_CLASSES
        train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, **kwargs)
        val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, **kwargs)
        test_loader = None

        return train_loader, val_loader, test_loader, num_class

    elif args.dataset == 'cityscapes':
        train_set = cityscapes.CityscapesSegmentation(args, split='train')
        val_set = cityscapes.CityscapesSegmentation(args, split='val')
        test_set = cityscapes.CityscapesSegmentation(args, split='test')
        num_class = train_set.NUM_CLASSES
        train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, **kwargs)
        val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, **kwargs)
        test_loader = DataLoader(test_set, batch_size=args.batch_size, shuffle=False, **kwargs)

        return train_loader, val_loader, test_loader, num_class
    elif args.dataset == 'vaihingen':
        train_set = vaihingen.Vaihingen(args, split='train')
        val_set = vaihingen.Vaihingen(args, split='val')
        num_class = train_set.NUM_CLASSES
        train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, **kwargs)
        print(train_loader)
        val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, **kwargs)
        print(val_loader)
        test_loader = None
        return train_loader, val_loader, test_loader, num_class

    elif args.dataset == 'landslide':
        trainpath = '/data/home/scv6559/run/xyl/1/path/train_noenhanced_path_list.csv'
        valpath = '/data/home/scv6559/run/xyl/1/path/val_path_list.csv'
        train_set = landslide.Landslide(args,trainpath ,split='train')
        val_set = landslide.Landslide(args,valpath, split='val')
        num_class = train_set.NUM_CLASSES
        train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, drop_last=True, **kwargs)
        print(train_loader)
        val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, drop_last=True, **kwargs)
        print(val_loader)
        test_loader = None
        return train_loader, val_loader, test_loader, num_class
        # train_set = landslide.Landslide(args, split='train')
        # val_set = landslide.Landslide(args, split='val')
        # num_class = train_set.NUM_CLASSES
        # train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, drop_last=True, **kwargs)
        # print(train_loader)
        # val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, drop_last=True, **kwargs)
        # print(val_loader)
        # test_loader = None
        # return train_loader, val_loader, test_loader, num_class



    else:
        raise NotImplementedError

