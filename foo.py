from loaders.loader_captured import SubjectLoaderTransientReal

loader = SubjectLoaderTransientReal(subject_id='cinema',
                                    root_fp='C:/Datasets/transient_nerf/cinema/final_cams/five_views',
                                    split='trainval',
                                    have_images=False)

print(loader)
