import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import os
import SimpleITK as sitk 

folder_path = '/Users/sarjhana/Desktop/Final Year Project/Data/AD'

images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
count = 0

for fig in images:

#fig = '/Users/sarjhana/Desktop/Final Year Project/AD/1 (1)1_deskull.nii'

    img = nib.load(fig)
    D = np.array(img.dataobj)

    D1 = D[:,:,128]      #axial
    D2 = D[:,128,:].T    #sagittal
    D3 = D[128,:,:].T    #coronal

    count += 1

    #Storing slices in dicom format
    filtered_image = sitk.GetImageFromArray(D1, "DICOMImageIO")
    sitk.WriteImage(filtered_image, "/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/AD_axial/%s.dcm"%(count))

    fil = sitk.GetImageFromArray(D2, "DICOMImageIO")
    sitk.WriteImage(fil, "/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/AD_sagittal/%s.dcm"%(count))

    fil1 = sitk.GetImageFromArray(D3, "DICOMImageIO")
    sitk.WriteImage(fil1, "/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/AD_coronal/%s.dcm"%(count))






















    #storing in nii format
    test = nib.Nifti1Image(D1, img.affine)
    nib.save(test, '/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/axial/%s.nii'%(count))

    test2 = nib.Nifti1Image(D2, img.affine)
    nib.save(test2, '/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/sagittal/%s.nii'%(count))

    test3 = nib.Nifti1Image(D3, img.affine)
    nib.save(test3, '/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/coronal/%s.nii'%(count))


'''
    D1 = np.int16(D1)
    D2 = np.int8(D2)
    D3 = np.int8(D3)

    #Storing slices in dicom format
    filtered_image = sitk.GetImageFromArray(D1, "DICOMImageIO")
    sitk.WriteImage(filtered_image, "/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/axial/%s.dcm"%(count))

    fil = sitk.GetImageFromArray(D2, "DICOMImageIO")
    sitk.WriteImage(fil, "/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/sagittal/%s.dcm"%(count))

    fil1 = sitk.GetImageFromArray(D3, "DICOMImageIO")
    sitk.WriteImage(fil1, "/Users/sarjhana/Desktop/Final Year Project/Data/AD_FINAL/coronal/%s.dcm"%(count))
'''


#tifffile.imsave('/Users/sarjhana/Desktop/Final Year Project/test.tif', D1)


'''
plt.figure()
plt.imshow(D1)
plt.show()

plt.figure()
plt.imshow(D2)
plt.show()

plt.figure()
plt.imshow(D3)
plt.show()
'''