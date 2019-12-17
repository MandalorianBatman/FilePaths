# FilePaths
Program to Merge and Represent File Paths.

Given a list of file paths as a string This program converts them in a nested dictionary where each key contains the children dictionaries of the folder

Consider **Input** as:

  'alpha/beta/gamma/delta alpha/beta/sigma beta/phi/pi/rho'
  
  The program **returns**:
  
    {'alpha': {'beta': {'gamma': {'delta': {}}, 'sigma': {}}}, 'beta': {'phi': {'pi': {'rho': {}}}}}
    
  and **Prints**:
  
    alpha
        beta
            gamma
                delta

            sigma
            
    beta
        phi
            pi
                rho

      
