Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

`1.3`_ (2018-10-02)
~~~~~~~~~~~~~~~~~~~

- Added ``HTTP_X_FORWARDED_FOR`` checking before ``REMOTE_ADDR`` for
  determining the remote IP of clicks.
- Removed code for really old Django versions. Dropped South migrations
  from the tree, regenerated migrations using a newer Django version for
  better compatbility.
- Reformatted the code using black.


`1.2`_ (2014-09-25)
~~~~~~~~~~~~~~~~~~~

- The version where this changelog starts.


.. _1.2: https://github.com/feincms/feincms-banners/commit/3d094f98187
.. _1.3: https://github.com/feincms/feincms-banners/compare/v1.2.0..v1.3.0
.. _Next version: https://github.com/feincms/feincms-banners/compare/v1.3.0...master
