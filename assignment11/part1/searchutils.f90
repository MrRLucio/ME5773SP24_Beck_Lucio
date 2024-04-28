MODULE searchutils

CONTAINS
    ! Description: Function that finds the location (idx) of a value x
    ! in an array using the linear search algorithm.
    !
    ! Find idx such that arr(idx) == x
    !
    FUNCTION linearSearch(arr, n, x) RESULT(idx)

        IMPLICIT NONE

        REAL(8) :: arr(n) ! Array to search
        INTEGER :: n ! Number of elements in array.
        REAL(8) :: x ! Value to search for in array.
        INTEGER :: idx ! Result of the search. [arr(idx) == x]

        ! Your implementation here.
        INTEGER :: counter 
        idx = -1 !if the loop makes no matches, it will return this "error code"
        DO counter = 1,n,1 !"count" was taken (Vim highlighted it in light blue)
            IF(arr(counter)==x) THEN
                idx = counter
                EXIT
            END IF
        END DO

    END FUNCTION linearSearch


    ! Description: Function that finds the location (idx) of a value x
    ! in a sorted array using the binary search algorithm.
    !
    ! Find idx such that arr(idx) == x
    !
    FUNCTION binarySearch(arr, n, x) RESULT(idx)

        IMPLICIT NONE

        REAL(8) :: arr(n) ! Array to search
        INTEGER :: n ! Number of elements in array.
        REAL(8) :: x ! Value to search for in array.
        INTEGER :: idx ! Result of the search. [arr(idx) == x]

        ! Your implementation here.
    
        INTEGER :: s ! Lower bound of the search span
        INTEGER :: m ! Mid value of the search span
        INTEGER :: e ! upper bound of the search span
        INTEGER :: clim ! counter limit.
        INTEGER :: counter ! The loop counter
    
        s = 1
        e = n
        m = INT(FLOOR(REAL(s+e)/2.0))
    
        idx = -1
        clim = INT(FLOOR(LOG(REAL(e))/LOG(2.0)) + 1)
    
        DO counter = 1,clim,1
            IF(arr(m)==x) THEN
                idx = m
                EXIT
            ELSE IF(arr(m) < x) THEN
                s = m+1
                m = INT(FLOOR(REAL(s+e)/2.0))
            ELSE
                e = m-1
                m = INT(FLOOR(REAL(s+e)/2.0))
            END IF
        END DO
        !idx = clim
    
    END FUNCTION binarySearch
END MODULE searchutils
